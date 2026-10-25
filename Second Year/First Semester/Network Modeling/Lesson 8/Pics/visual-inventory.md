# Lesson 8 visual inventory

Source: `../Lesson 8.pdf`. All seven original visual units were inspected directly. Current figures preserve the original mechanisms and qualitative profiles, but use a clearer layout, consistent input/output colors, labelled areas and short event markers. Copied margin prose has been removed. Source crops remain available for comparison. Curved profiles are schematic; no measured numerical samples or time coordinates are claimed.

Pink denotes source input, dashed blue denotes shaper output, orange denotes queued data, and green denotes recovered credits. In the two curved plots, the queue-empty time is obtained from equal accumulation/drainage areas of the schematic profile, rather than an arbitrary endpoint. The last figure uses three aligned panels to distinguish traffic rates, token content and queue content. Its time origin is the end of the first alarm, matching the text.

|Source page|Visual unit and meaningful stages|Destination section|Asset|
|---|---|---|---|
|1|Token bucket, input queue, output queue, link, rate labels and sizing formulas|Little recap from lesson 7|01-shaper-and-link-redrawn.svg|
|1|Input above declared peak; token depletion, forwarded area, accumulated backlog and later drainage|Question|02-above-declared-peak-redrawn.svg|
|1|Input below declared peak; longer unbuffered interval, rate reduction, equal-area drainage and depletion-time comparison|Other scenario, same setting|03-below-declared-peak-redrawn.svg|
|2|Packet timeline: low-frequency reports, first alarm, normal reports and second alarm|Source|04-sensor-packets-redrawn.svg|
|2|Fluid rate profile, both alarms, normal level, alarm duration, reward area and interval between alarm starts|Source|05-sensor-fluid-profile-redrawn.svg|
|3|Empty-bucket alarm sketch, shaded forwarded/queued amounts, total alarm bytes and comparison with queued excess|What's the PDF of # of|06-empty-bucket-alarm-redrawn.svg|
|4|Embedded board photograph: first alarm, normal interval, recovered credits, second alarm and area A|What's the PDF of # of|07-board-two-alarms-redrawn.svg|

The packet timeline uses representative stems, with explicit spacing labels and a caption stating that time is not to scale. The adjacent rectangles in the original empty-bucket sketch represent two consecutive alarms. The corrected figure preserves both: the first is fully forwarded; stored tokens run out at its end, so the second alarm is split into forwarded and queued amounts. The earlier single-alarm redesign lost this temporal context and has been replaced. The board photo is expanded into aligned rate, token and backlog panels. These layout changes supersede the earlier literal reproductions.

Every row has a working embed in `../8. Token bucket shaping and random alarms - Integrated notes.md`. Regenerate SVG figures and high-resolution PNG copies with `python3 redraw_figures.py` (rsvg-convert required). Regenerate retained source crops with `python3 extract_figures.py` (PyMuPDF required). Both scripts run from any directory.

# Source coverage check

|Transcript interval|Integrated destination|
|---|---|
|00:00:26–00:09:30|Recap, SLA, bucket and buffer sizing|
|00:09:34–00:19:29|Question: token exhaustion, rate decrease versus loss, backlog accumulation and drainage|
|00:19:37–00:27:23|Other scenario and burst-duration comparison|
|00:27:27–00:35:08|Practical modelling task and sensor source|
|00:45:54–01:03:05|Long-term mean, renewal reward, peak, duration and bucket sizing|
|01:03:07–01:14:25|Grace period, random recovery time, initial conditions and buffering probability|
|01:14:27–01:19:00|Random queued amount; density versus probability mass|
|01:19:12–01:34:31|Alarm bytes, token-depletion time, backlog transformation and distribution|

Administrative comments, student work time and unrelated/garbled speech are omitted. The complete transcript was read. No Moodle files are present in Lesson 8; the related chapter in Lesson 7 was consulted for token-bucket definitions and buffer-sizing conditions (printed pp. xi–xv, PDF pp. 4–8). Its distinct hard peak-rate parameter is explicitly distinguished from the lecture's uncapped example. No supplementary figure is needed to explain additional geometry: the original topology already supplies both queues and the link.

Unresolved source-model issue: Poisson alarm starts can overlap fixed-duration alarm states, but overlap handling is unspecified. The lecture also changes its interval origin between the renewal-reward calculation and the recovery calculation. The integrated note flags both points and presents the final distribution conditional on the stated empty-queue/empty-bucket starting state, rather than as a stationary result.

All seven revised diagrams were rendered to PNG and inspected for readability and consistency with the source mechanisms and integrated explanations. PNG copies use the same basename as the SVG assets.

Figure 06 correction: time zero is the start of the first alarm; token exhaustion occurs at D = T_b, when the second starts immediately (δ = 0). The input stays high at this boundary while the output drops to ρ. This restores the original sequence; only the second alarm starts with an empty bucket.
