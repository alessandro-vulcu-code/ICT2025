#set terms(hanging-indent: 1.5em)

#set table(
  inset: 6pt,
  stroke: none
)

#let horizontalRule = line(start: (25%,0%), end: (75%,0%))
// Polyfill divider to allow compiling with typst < 0.15:
#let divider = if "divider" in std { divider } else { horizontalRule }

#show figure.where(
  kind: table
): set figure.caption(position: top)

#show figure.where(
  kind: image
): set figure.caption(position: bottom)

#let content-to-string(content) = {
  if content.has("text") {
    content.text
  } else if content.has("children") {
    content.children.map(content-to-string).join("")
  } else if content.has("body") {
    content-to-string(content.body)
  } else if content == [ ] {
    " "
  }
}
#let conf(
  title: none,
  subtitle: none,
  authors: (),
  keywords: (),
  date: none,
  abstract-title: none,
  abstract: none,
  thanks: none,
  cols: 1,
  margin: (x: 1.25in, y: 1.25in),
  paper: "us-letter",
  lang: "en",
  region: "US",
  font: none,
  fontsize: 11pt,
  mathfont: none,
  codefont: none,
  linestretch: 1,
  sectionnumbering: none,
  linkcolor: none,
  citecolor: none,
  filecolor: none,
  pagenumbering: "1",
  doc,
) = {
  set document(
    title: title,
    keywords: keywords,
  )
  set document(
      author: authors.map(author => content-to-string(author.name)).join(", ", last: " & "),
  ) if authors != none and authors != ()
  set page(
    paper: paper,
    margin: margin,
    numbering: pagenumbering,
    columns: cols
  )

  set par(
    justify: true,
    leading: linestretch * 0.65em
  )
  set text(lang: lang,
           region: region,
           size: fontsize)

  set text(font: font) if font != none
  show math.equation: set text(font: mathfont) if mathfont != none
  show raw: set text(font: codefont) if codefont != none

  set heading(numbering: sectionnumbering)

  show link: set text(fill: rgb(content-to-string(linkcolor))) if linkcolor != none
  show ref: set text(fill: rgb(content-to-string(citecolor))) if citecolor != none
  show link: this => {
    if filecolor != none and type(this.dest) == label {
      text(this, fill: rgb(content-to-string(filecolor)))
    } else {
      text(this)
    }
  }

  if title != none {
    place(top, float: true, scope: "parent", clearance: 4mm, block(below: 1em, width: 100%)[
      #if title != none {
        align(center, block[
            #text(weight: "bold", size: 1.5em, hyphenate: false)[#title #if thanks != none {
                footnote(thanks, numbering: "*")
                counter(footnote).update(n => n - 1)
              }]
            #(
              if subtitle != none {
                parbreak()
                text(weight: "bold", size: 1.25em, hyphenate: false)[#subtitle]
              }
             )])
      }

      #if authors != none and authors != [] {
        let count = authors.len()
        let ncols = calc.min(count, 3)
        grid(
          columns: (1fr,) * ncols,
          row-gutter: 1.5em,
          ..authors.map(author => align(center)[
            #author.name \
            #author.affiliation \
            #author.email
          ])
        )
      }

      #if date != none {
        align(center)[#block(inset: 1em)[
            #date
          ]]
      }

      #if abstract != none {
        block(inset: 2em)[
          #text(weight: "semibold")[#abstract-title] #h(1em) #abstract
        ]
      }
    ])
  }
  doc
}
#show: doc => conf(
  abstract-title: [Abstract],
  pagenumbering: "1",
  cols: 1,
  doc,
)


= 1. Introduction, preferences and decision problems
<introduction-preferences-and-decision-problems>
== Prerequisites you need
<prerequisites-you-need>
Game theory studies situations in which several decision makers affect
one another's results. In the notation used here, a set such as
$A = { r\,s }$ collects possible alternatives, and $a in A$ means that
$a$ is one of them. A function assigns a value to each input:
$u\(r\)= 5$, for example, assigns utility 5 to alternative $r$. The
symbols $forall$ and $arrow.l.r.double$ mean “for every” and “if and
only if.” A higher utility represents a more preferred outcome.

== 1. Games and strategic interaction
<games-and-strategic-interaction>
#emph[Gth2001.pdf, PDF pp.~3--13.]

In a one-person decision problem, a decision maker selects an available
action and evaluates the resulting outcome. In a game, each player's
result depends on the actions chosen by several players. A person, firm,
or network device can act as a player; its action is one of its
available choices, and its payoff represents how it ranks the resulting
outcome. Payoffs are player-specific: the same outcome can be valuable
to one player and undesirable to another.

#quote(block: true)[
#strong[Definition — Game.] A game models interaction between multiple
players whose outcomes depend on their joint choices.
]

Players are commonly assumed to know the rules and to choose rationally
according to their own preferences. Knowing the rules does not mean
observing another player's choice before acting. If player $i$ chooses
action $a_i$, their payoff can be written $u_i\(a_1\,dots.h\,a_n\)$,
where $a_1\,dots.h\,a_n$ are the actions selected by all $n$ players.
There need not be one objective that all players maximize together.

=== Lecture example --- transmission choices
<lecture-example-transmission-choices>
#emph[Gth2001.pdf, PDF p.~12; illustrative payoff matrix below spells
out the transmission example.]

Two devices independently choose whether to transmit ($T$) or wait
($W$). A successful transmission gives payoff 2, a collision gives
payoff $- 1$, and waiting gives payoff 0. Neither device observes the
other's choice before deciding. Each cell lists payoffs in the order
$\(u_1\,u_2\)$, with device 1's payoff first.

#figure(
  align(center)[#table(
    columns: 3,
    align: (auto,auto,auto,),
    table.header([Device 1 / Device 2], [$T$], [$W$],),
    table.hline(),
    [$T$], [$\(- 1\,- 1\)$], [$\(2\,0\)$],
    [$W$], [$\(0\,2\)$], [$\(0\,0\)$],
  )]
  , kind: table
  )

Device 1's preferred action depends on device 2's choice. If device 2
waits, transmitting gives device 1 payoff 2 rather than 0. If device 2
transmits, waiting gives 0 rather than $- 1$. So the best choice cannot
be determined by looking at device 1 in isolation.

The same kind of interaction appears in markets, auctions, bargaining,
distributed systems, access to shared resources, network cooperation,
voting, and online platforms. A useful model retains incentives relevant
to the question while keeping the analysis manageable.

== 2. Markets and rewards over time
<markets-and-rewards-over-time>
#emph[Gth2001.pdf, PDF pp.~15--19.]

A #strong[monopoly] has one supplier; an #strong[oligopoly] has a small
number of suppliers whose decisions affect one another. Firms that
coordinate through a trust or collusive agreement can act like a single
supplier. A profit-maximizing firm pursues its own profit, which need
not maximize consumer welfare. Competitive and monopoly prices provide
useful benchmarks, but their comparison depends on demand, costs, and
market rules.

=== Substitute goods
<substitute-goods>
Goods are #strong[substitutes] when an increase in the price of one
increases demand for the other, holding other relevant conditions fixed.
Butter and margarine, and coffee and tea, are examples. This cross-price
effect differs from the usual own-price effect, where demand for a good
falls as its own price rises. Giffen and Veblen goods are mentioned as
exceptions to that usual pattern.

=== Discount factor
<discount-factor>
A reward received later can be expressed in today's value using a
discount factor. If $0 < delta < 1$, a reward $x$ received $t$ periods
from now has present value $delta^t x$. Here $t = 0$ means today, and
each additional period applies the factor once more. Discounting can
represent impatience, deterioration, inflation, uncertainty, or a
constant probability of continuing to participate.

== 3. Decision problems and preferences
<decision-problems-and-preferences>
#emph[Gth2001.pdf, PDF pp.~21--22.]

A decision problem identifies available actions, the outcomes they
produce, and how those outcomes are ranked. Write $a succ.curly.eq b$
when alternative $a$ is at least as good as $b$. Strict preference,
$a succ b$, means $a$ is preferred to $b$ but not vice versa;
indifference, $a tilde.op b$, means both alternatives are equally
preferred.

A preference is #strong[complete] if every pair of alternatives can be
compared: for all $a\,b in A$, either $a succ.curly.eq b$,
$b succ.curly.eq a$, or both. It is #strong[transitive] if
$a succ.curly.eq b$ and $b succ.curly.eq c$ imply $a succ.curly.eq c$. A
rational preference relation satisfies both properties. Completeness
also gives reflexivity, since setting $a = b$ yields
$a succ.curly.eq a$.

=== Lecture example --- indifference and inconsistent rankings
<lecture-example-indifference-and-inconsistent-rankings>
#emph[Gth2001.pdf, PDF p.~22.]

For alternatives $A = { r\,s\,v }$, suppose ravioli ($r$) and vegetables
($v$) are equally preferred, and both are preferred to soup ($s$):
$r tilde.op v succ s$. Every pair can be compared consistently, so the
preference is complete and transitive. Equal preference does not make
ravioli and vegetables the same alternative.

By contrast, $r succ s$, $s succ v$, and $v succ r$ form a cycle.
Transitivity would require $r succ v$, contradicting $v succ r$. A
person unable to compare two alternatives at all also violates
completeness; that differs from indifference, which is a definite
judgment that neither alternative is preferred.

#quote(block: true)[
#strong[Terminology correction — Gth2001.pdf, PDF p. 22.] With
indifference between distinct alternatives allowed, a complete and
transitive weak preference is a #strong[total preorder]. It need not be
antisymmetric, so it is not necessarily a total order. Antisymmetry
would rule out distinct alternatives such as $r$ and $v$ being equally
preferred.
]

== 4. Utility as a representation of preference
<utility-as-a-representation-of-preference>
#emph[Gth2001.pdf, PDF pp.~23--26.]

A utility function represents a preference ranking by assigning numbers
that preserve its order:

#quote(block: true)[
#strong[Definition — Utility representation.] A function
$u : A arrow.r bb(R)$ represents $succ.curly.eq$ when, for every
$a\,b in A$,

$ a succ.curly.eq b arrow.l.r.double u\(a\)gt.eq u\(b\). $
]

Equal utility corresponds to indifference, while higher utility
corresponds to strict preference. For $r tilde.op v succ s$, values
$u\(r\)= u\(v\)= 2$ and $u\(s\)= 1$ preserve the ranking. These
utilities are #strong[ordinal]: their order matters, not the size of the
differences. Assignments 5 and 1 and assignments 25 and 1 represent the
same ranking between two alternatives.

#quote(block: true)[
#strong[Theorem — Utility representation on a finite set.] A
preference on finite set $A$ has a real-valued utility representation if
and only if it is complete and transitive.
]

Any utility representation is complete and transitive because real
numbers can be compared and their ordering is transitive. Conversely,
for a finite set, one construction assigns each alternative the number
of alternatives it weakly outranks:

$ u\(a\)= lr(|{ b in A : a succ.curly.eq b }|) . $

For $r tilde.op v succ s$, soup weakly outranks only itself, while
ravioli and vegetables weakly outrank all three alternatives. This gives
$u\(s\)= 1$ and $u\(r\)= u\(v\)= 3$, representing the same ranking as
$\(2\,1\,2\)$ in order $\(r\,s\,v\)$. Ties receive equal values; strict
preference produces a larger count. The construction relies on $A$ being
finite.

For a desirable quantity $q$, the slides also consider utility functions
with $u'\(q\)gt.eq 0$ and $u''\(q\)lt.eq 0$. The first condition means
that more does not reduce utility; the second means that marginal
utility does not increase. These are assumptions about the model, not
consequences of rational preferences.

== 5. Decision trees and one-person optimization
<decision-trees-and-one-person-optimization>
#emph[Gth2001.pdf, PDF pp.~27--31.]

A decision tree represents choices as branches from a starting node to
terminal outcomes. When one decision maker controls all choices and
knows the consequences, the best complete path is the one with highest
terminal utility. At intermediate nodes, compare the utilities
attainable from each continuation.

=== Lecture example --- choosing lunch
<lecture-example-choosing-lunch>
#emph[Gth2001.pdf, PDF pp.~28--31.]

The student first chooses ravioli ($r$) or soup ($s$), then fish ($f$)
or vegetables ($v$). The terminal utilities are 8 for $r f$, 7 for
$r v$, 4 for $s f$, and 3 for $s v$.

#figure(image("Pics/gth2001-p29-canteen-tree.png", alt: "Canteen decision tree: choose ravioli or soup, then fish or vegetables, with terminal utilities 8, 7, 4, and 3."),
  caption: [
    Canteen decision tree: choose ravioli or soup, then fish or
    vegetables, with terminal utilities 8, 7, 4, and 3.
  ]
)

#emph[Figure 1. Canteen decision tree. Source: Gth2001.pdf, PDF p.~29.
Parenthesized values 5 and 1 refer to the earlier starter-only example;
terminal values determine this expanded choice.]

Solve from the final choices back to the start:

+ After ravioli, choose fish because $8 > 7$.
+ After soup, choose fish because $4 > 3$.
+ At the first choice, compare the best continuation values, 8 and 4.
  Choose ravioli.

The optimal meal is $r f$, with utility 8. The values in parentheses on
the tree are not additional rewards to add to terminal utilities.

The same problem can be written as a single choice among complete meals:

#figure(image("Pics/gth2001-p31-collapsed-tree.png", alt: "Flattened decision tree listing complete meals rf, rv, sf, and sv with utilities 8, 7, 4, and 3."),
  caption: [
    Flattened decision tree listing complete meals rf, rv, sf, and sv
    with utilities 8, 7, 4, and 3.
  ]
)

#emph[Figure 2. Complete meals and terminal utilities. Source:
Gth2001.pdf, PDF p.~31.]

$ A = { r f\,r v\,s f\,s v }\,#h(2em) max_(a in A) u\(a\)= 8\,#h(2em) "arg max"_(a in A) u\(a\)= { r f } . $

The maximum is the utility value; the arg max is the set of choices that
attain it. If multiple alternatives tie for the maximum, each belongs to
the arg max. Flattening works because one informed decision maker
controls every choice. In a game involving multiple players, each player
controls their own decisions, so one player's utility cannot determine
every branch.
