<!-- Pagina 1 -->

C++ Standard Library

Modern C++ Programming for ICT
Filippo Campagnaro
campagn1@dei.unipd.it

---

**Immagini estratte:**

![Figura estratta 1](images/p01_img01.jpg)

![Figura estratta 2](images/p01_img04.jpg)

![Figura estratta 3](images/p01_img03.jpg)

![Figura estratta 4](images/p01_img02.jpg)


---

<!-- Pagina 2 -->

Outline

1. Standard library design
2. Containers
3. Iterators
4. Algorithms
5. Strings
6. I/O Streams

[c++pl] Chapter 30-33, 36, 38

---

**Immagini estratte:**

![Figura estratta 1](images/p02_img01.jpg)


---

<!-- Pagina 3 -->

C++ standard library

It is specified by the ISO C++ standard, and provided by any C++ implementations

• it supports language features (e.g., run-time type information, memory management, range-for loops)
• it provides information on implementation-defined features, e.g., the maximum/minimum value for a certain numeric type
• it supports concurrent programming
• it implements primitives for programming (containers, algorithms, etc)
• it has basic math functions

---

**Immagini estratte:**

![Figura estratta 1](images/p03_img01.jpg)


---

<!-- Pagina 4 -->

C++ standard library

By design, it is

1. portable – the code that uses standard library features can be used on different operative systems, compilers, etc
2. efficient – the code that uses the standard library is computationally efficient
3. a foundation for other libraries, which can reuse what is defined in the standard library instead that re-invent the wheel

It is defined in a set of headers for the std namespace

---

**Immagini estratte:**

![Figura estratta 1](images/p04_img01.jpg)


---

<!-- Pagina 5 -->

stdlib containers

A container holds multiple objects
• in a sequence (sequence containers)
• in a structure which can be accessed through key-based lookups (associative containers)

Containers can be seen as resource handles, with well defined copy and move operations

In the next slides, we will provide a list of useful stdlib types, without many details – the goal is to give you an overview, for details use cppreference.com

---

**Immagini estratte:**

![Figura estratta 1](images/p05_img01.jpg)


---

<!-- Pagina 6 -->

stdlib containers

Containers are implemented using templates, with template types for the

• type of object
• allocator, i.e., the function used to allocate and release memory resources – by default `std::allocator<T>` is the pair `new/delete` on objects of type T
• key (if required)
• type of comparison (if required) – for example `<, =`
• a hash function (if required)

It is possible to obtain the size of a container (`c.size()`), check it is empty (`c.empty()`), etc

---

**Immagini estratte:**

![Figura estratta 1](images/p06_img01.jpg)


---

<!-- Pagina 7 -->

Sequence containers

1. `std::vector<T, A>`  
   contiguous allocation

2. `std::deque<T, A>`

3. `std::list<T, A>`  
   non-contiguous allocation

4. `std::forward_list<T, A>`  
   type of the object in the container

   type of the allocator, by default `std::allocator<T>` (no need to change it unless for specific reasons)

in general, use `std::vector<T>` unless you have other specific needs

---

**Immagini estratte:**

![Figura estratta 1](images/p07_img01.jpg)


---

<!-- Pagina 8 -->

Sequence containters

Examples of usage:

```cpp
std::vector<int> vec {1, 2, 3, 4};

std::list<int> ls {1, 2, 3, 4};
```

---

**Immagini estratte:**

![Figura estratta 1](images/p08_img01.jpg)


---

<!-- Pagina 9 -->

Ordered associative containers

1. `std::map<K, V, C, A>` ordered map from K to V (ordered by key)
2. `std::multimap<K, V, C, A>` ordered map from K to V (ordered by key), it allows multiple entries with the same key
3. `std::set<K, C, A>` ordered set of elements with value K
4. `std::multiset<K, C, A>` ordered set of elements with value K, it allows multiple entries with the same value

---

**Immagini estratte:**

![Figura estratta 1](images/p09_img01.jpg)


---

<!-- Pagina 10 -->

Ordered associative containers

This is an example of std::map usage

```cpp
std::map<int, std::string> map_int_s;

map_int_s.insert(std::make_pair(4, "four"));
map_int_s[5] = "five";
// this updates the value associated with
// the key, if present, or it performs the
// insertion otherwise.

auto entry_it = map_int_s.find(4);
```

---

**Immagini estratte:**

![Figura estratta 1](images/p10_img01.jpg)


---

<!-- Pagina 11 -->

Map element access

```cpp
//SOL1 : use []
std::string s1 = map_int_s[7]; // if k = 7
// is not present, it adds map_int_s[7] =
// std::string{} and returns it

//SOL2: use find() → best option
auto entry_it = map_int_s.find(4);
if(entry_it ≠ map_int_s.end()) {
    std::string s2 = entry_it.second()
} // it uses iterators: if k = 4 is not
// present, it returns map_int_s.end()
```

---

**Immagini estratte:**

![Figura estratta 1](images/p11_img01.jpg)


---

<!-- Pagina 12 -->

Unordered associative containers

1. `std::unordered_map<K, V, H, E, A>` unordered map from K to V
   type of the key
   type of the value
   equality test, by default
   `std::equal_to<K>`
   type of the allocator
   hash function to project the key into a searchable space, by default `std::hash<K>`

2. `std::unordered_multimap<K, V, H, E, A>` unordered map from K to V, it allows multiple entries with the same key

3. `std::unordered_set<K, H, E, A>` unordered set of elements with value K

4. `std::unordered_multiset<K, H, E, A>` unordered set of elements with value K, it allows multiple entries with the same value

---

**Immagini estratte:**

![Figura estratta 1](images/p12_img01.jpg)


---

<!-- Pagina 13 -->

Container adaptors

They are not containers, they just provide interfaces to other containers for specific functions (in particular, push and pop operations)

1. `std::priority_queue<T, C, Cmp>`  
   it creates a priority queue out of the elements of type T in the container C (by default `std::vector<T>`), according to the priority set by the function Cmp

2. `std::queue<T, C>`  
   queue of elements of type T in a container C (by default `std::deque<T>`)

3. `std::stack<T, C>`  
   stack of elements of type T in a container C (by default `std::vector<T>`)

---

**Immagini estratte:**

![Figura estratta 1](images/p13_img01.jpg)


---

<!-- Pagina 14 -->

Almost containers

Sequences of elements without all the facilities defined for a full-fledged container

1. `std::array<T, N>` size of the array
   fixed-size array, it cannot be enlarged or reduced as containers

2. `std::basic_string<C, Tr, A>` basic representation of a string, more on this later

---

**Immagini estratte:**

![Figura estratta 1](images/p14_img01.jpg)


---

<!-- Pagina 15 -->

Operations on containers

Container:
value_type, size_type, difference_type, pointer, const_pointer, reference, const_reference
iterator, const_iterator, ?reverse_iterator, ?const_reverse_iterator, allocator_type
begin(), end(), cbegin(), cend(), ?rbegin(), ?rend(), ?crbegin(), ?crend(), =, ==, !=
swap(), ?size(), max_size(), empty(), clear(), get_allocator(), constructors, destructor
?<, ?<=, ?>, ?>=, ?insert(), ?emplace(), ?erase()

Sequence container:
assign(), front(), resize()
?back(), ?push_back()
?pop_back(), ?emplace_back()

Assocative container:
key_type, mapped_type, ?[], ?at()
lower_bound(), upper_bound(), equal_range()
find(), count(), emplace_hint()

Ordered container:
key_compare
key_comp()
value_comp()

Hashed container:
key_equal(), hasher
hash_function()
key_equal()
bucket interface

List:
remove()
remove_if(), unique()
merge(), sort()
reverse()

splice()
list

insert_after(), erase_after()
emplace_after(), splice_after()

forward_list

vector

map

set

unordered_map

multimap

unordered_set

multiset

unordered_multimap

unordered_multiset

---

**Immagini estratte:**

![Figura estratta 1](images/p15_img01.jpg)


---

<!-- Pagina 16 -->

# Member types for containers

| Member types (§iso.23.2, §iso.23.3.6.1) |
| :--- |
| `value_type` Type of element |
| `allocator_type` Type of memory manager |
| `size_type` Unsigned type of container subscripts, element counts, etc. |
| `difference_type` Signed type of difference between iterators |
| `iterator` Behaves like `value_type*` |
| `const_iterator` Behaves like `const_value_type*` |
| `reverse_iterator` Behaves like `value_type*` |
| `const_reverse_iterator` Behaves like `const_value_type*` |
| `reference` `value_type&` |
| `const_reference` `const_value_type&` |
| `pointer` Behaves like `value_type*` |
| `const_pointer` Behaves like `const_value_type*` |
| `key_type` Type of key; associative containers only |
| `mapped_type` Type of mapped value; associative containers only |
| `key_compare` Type of comparison criterion; ordered containers only |
| `hasher` Type of hash function; unordered containers only |
| `key_equal` Type of equivalence function; unordered containers only |
| `local_iterator` Type of bucket iterator; unordered containers only |
| `const_local_iterator` Type of bucket iterator; unordered containers only |

page 896, c++pl

---

**Immagini estratte:**

![Figura estratta 1](images/p16_img01.jpg)


---

<!-- Pagina 17 -->

Iterators

Similar to a pointer, they can be used to iterate over a sequence

begin()
++ to go to the next
value
element after the last valid one
sequence
* to get the value

containers iterators algorithms

Iterators separate containers from algorithms, so that the same algorithm implementation can be used on different containers

---

**Immagini estratte:**

![Figura estratta 1](images/p17_img01.jpg)


---

<!-- Pagina 18 -->

## Iterators

### • Input/output iterators
for streams, without end

Operators defined for each iterator family

$$\text{++ (go to next),}$$
$$\star (\text{dereference})$$

### • Forward iterators
for sequences, only move forward sequentially

$$\text{++, *},$$
$$\equiv (\text{equal to}),$$
$$\neq (\text{different from}),$$
$$\rightarrow (\text{access to public members of the object pointed by the iterator})$$

### • Bidirectional iterators
move forward/backward sequentially

$$\text{++, *}, \equiv, \neq, \rightarrow,$$
$$\text{-- (go to previous)}$$

### • Random access iterators
move forward/backward or access any position in the sequence, not necessarily following a sequential order

$$\text{++, *}, \equiv, \neq, \rightarrow, \text{--},$$
$$\equiv, \text{+= (skip forward or backward multiple steps)},$$
$$[\text{] (access with index)},$$
$$<, \leq, >, \geq (\text{comparisons})$$

---

**Immagini estratte:**

![Figura estratta 1](images/p18_img01.jpg)


---

<!-- Pagina 19 -->

Iterators

```cpp
std::vector<int> vec {1,2,3,4};
std::vector<int>::iterator vec_iter = vec.begin();
std::vector<int>::iterator vec_end = vec.end();

while(vec_iter ≠ vec_end)
{
    // this increases the value in the vector,
    // e.g, 1++ → 2
    ++(*vec_iter);
    // this increases the value of the iterator,
    // i.e., the entry to which the iterator points
    ++vec_iter;
}
```

There is also a const_iterator for read-only operations

---

**Immagini estratte:**

![Figura estratta 1](images/p19_img01.jpg)


---

<!-- Pagina 20 -->

Algorithms

• The standard library contains the implementation of ~80 generic algorithms, which (in most cases) can operate on any of the containers defined in the stdlib

• They are defined in the `<algorithm>` header

• Search, find, transform, sort, etc

• The algorithms can operate using
  • conventional operators for comparison (<, ==, !=, etc)
  • custom, user-defined versions of the comparisons (key operations, with a function f(i1, i2) applied on two elements)

---

**Immagini estratte:**

![Figura estratta 1](images/p20_img01.jpg)


---

<!-- Pagina 21 -->

Algorithms

• The algorithms operate on sequences, exploiting iterators

containers iterators algorithms

• A pair of iterators [b, e] defines the input sequence
• A single iterator defines the output, which is assumed to have enough elements (for example, as many as e–b)
  • this is not guaranteed: always check the ranges of the sequences passed to the algorithms
  • this is due to the fact that iterators do not exactly match the definition of a sequence, but this abstraction avoids the re-implementation of the algorithm for each type of container

---

**Immagini estratte:**

![Figura estratta 1](images/p21_img01.jpg)


---

<!-- Pagina 22 -->

Complexity

Algorithm Complexity (§iso.25)

O(1) swap(), iter_swap()
O(log(n)) lower_bound(), upper_bund(), equal_range(), binary_search(), push_heap(), pop_heap()
O(n*log(n)) inplace_merge() (worst case), stable_partition() (worst case),
sort(), stable_sort(), partial_sort(), partial_sort_copy(), sort_heap()
O(n*n) find_end(), find_first_of(), search(), search_n()
O(n) All the rest

• The worst complexity (asymptotically) is O(n²)
• They are some of the most efficient implementations available

---

**Immagini estratte:**

![Figura estratta 1](images/p22_img01.jpg)


---

<!-- Pagina 23 -->

Non-modifying sequence algorithms

Sequence predicates
• all_of(begin, end, fun)
• any_of(begin, end, fun)
• none_of(begin, end, fun)

fun makes a Boolean check on all the elements, and the predicates return
true if fun is always true
true if fun is true at least once
true if fun is always false

count (begin, end, v)
counts how many elements are equal to v

p=find (begin, end, v)
p points to the first element between begin and end equal to v (if no match, p=end)

---

**Immagini estratte:**

![Figura estratta 1](images/p23_img01.jpg)


---

<!-- Pagina 24 -->

Non-modifying sequence algorithms

equal (begin, end, begin2)
checks if the elements from begin to end are equal to those in the sequence starting from begin2

p=mismatch (begin, end, begin2)
p points to the first element from begin to end that is not equal to that in the same position in the sequence starting from begin2

search (begin, end, begin2, end2)
search if the sequence from begin2 to end2 is in the larger sequence from begin to end

---

**Immagini estratte:**

![Figura estratta 1](images/p24_img01.jpg)


---

<!-- Pagina 25 -->

Non-modifying/modifying sequence alg

for_each(begin, end, fun)
applies fun to every element from begin to end according to the behavior of fun, they may be modified or not

transform(begin, end, out, fun)
applies fun to the elements from begin to end that are copied to out (the original element is not modified, unless out=begin)

---

**Immagini estratte:**

![Figura estratta 1](images/p25_img01.jpg)


---

<!-- Pagina 26 -->

Modifying sequence algorithms

copy(begin, end, out)
copies the sequence from begin to end to out

unique(begin, end)
removes adjacent duplicates

remove(begin, end, v)
removes elements with value v

replace(begin, end, v, v2)
replaces elements equal to v with value v2

---

**Immagini estratte:**

![Figura estratta 1](images/p26_img01.jpg)


---

<!-- Pagina 27 -->

Modifying sequence algorithms

rotate(begin, m, end)
rotate elements by m positions

$$\begin{array}{c|c|c|c}
1 & 2 & 3 & 4 \\
\hline
m = \text{begin} + 1 \\
\end{array}$$

random_shuffle(begin, end)
shuffle randomly the elements from begin to end

next_permutation(begin, end)
make [begin:end] the next permutation (lexicographical order)

swap(x, y)
swaps the values of x and y

---

**Immagini estratte:**

![Figura estratta 1](images/p27_img01.jpg)


---

<!-- Pagina 28 -->

Sort and search

• the stdlib offers multiple options for sorting containers
  • for example: `std::sort(begin, end)`

• binary_search algorithms provide binary search in ordered containers

• it is also possible to merge two ordered containers

• it is possible to find the min and max elements in a container

---

**Immagini estratte:**

![Figura estratta 1](images/p28_img01.jpg)


---

<!-- Pagina 29 -->

C++ strings

• strings are implemented with a template that accepts different kinds of character types
• the characters are stored contiguously (as in an array)

```cpp
template<typename C,
typename Tr = char_traits<C>,
typename A = allocator<C>>
class basic_string {
public:
    using traits_type = Tr;
    using value_type = typename Tr::char_type;
    using allocator_type = A;
    using size_type = typename allocator_traits<A>::size_type;
    using difference_type = typename allocator_traits<A>::difference_type;
    using reference = value_type&;
    using const_reference = const value_type&;
    using pointer = typename allocator_traits<A>::pointer;
    using const_pointer = typename allocator_traits<A>::const_pointer;
    using iterator = /* implementation-defined */;
    using const_iterator = /* implementation-defined */;
    using reverse_iterator = std::reverse_iterator<iterator>;
    using const_reverse_iterator = std::reverse_iterator<const_iterator>;

    static const size_type npos = -1; // integer representing end-of-string
};
```

---

**Immagini estratte:**

![Figura estratta 1](images/p29_img01.jpg)


---

<!-- Pagina 30 -->

C++ strings

There are some specializations of the basic_string template already available

• using std::string = std::basic_string<char>
• using std::wstring = std::basic_string<wchar>

There are multiple constructors, the most useful are

```cpp
std::string empty {}; // default
std::string c_style {"this is a C-style string"};
std::string another {c_style}; // copy
```

---

**Immagini estratte:**

![Figura estratta 1](images/p30_img01.jpg)


---

<!-- Pagina 31 -->

C++ strings

It is possible to perform multiple operations on strings:

• comparisons
• size, length, resize
• access to characters
• numeric conversions
• stdlib-like operations: find, replace, etc
• extraction and manipulation of substrings

---

**Immagini estratte:**

![Figura estratta 1](images/p31_img01.jpg)


---

<!-- Pagina 32 -->

I/O streams

• I/O streams convert typed-values to sequences of bytes

Typed value
‘c’ 123
ostream
istream
fstream can do both

byte sequence in buffer

terminal, file, string, keyboard, etc

Streams are
• type-safe
• extensible
• sensitive to locale settings
• efficient

---

**Immagini estratte:**

![Figura estratta 1](images/p32_img01.jpg)


---

<!-- Pagina 33 -->

I/O streams

• Predefined standard stream objects are automatically created at program startup if `<iostream>` is #included
  • `std::cout`, `std::cerr`, `std::clog`, `std::cin`

• The other stdlib I/O stream facilities are organized in a hierarchy:

```markdown
ios_base
basic_ios
basic_istream
basic_ostream
basic_istringstream
basic_iostream
basic_ostringstream
basic_ifstream
basic_ofstream
basic_fstream
basic_stringstream
```

---

**Immagini estratte:**

![Figura estratta 1](images/p33_img01.jpg)


---

<!-- Pagina 34 -->

File streams

• File streams open, read, write and close files
• Defined in the `<fstream>` header
  • ifstream to read a file
  • ofstream to write to a file
  • fstream to do both
• Open a file

```cpp
#include <fstream>
string filename = "test.txt";
// open the file, multiple options available
// (e.g., append, replace, etc)
std::ofstream fout(filename.c_str());
if (!fout) // check if opened correctly
{
    std::cout << "error: open file for output failed!"
            << std::endl;
    exit(127);
}
```

---

**Immagini estratte:**

![Figura estratta 1](images/p34_img01.jpg)


---

<!-- Pagina 35 -->

File streams

• Write to a file
  fout << "a line" << std::endl
  fout << "another line" << std::endl

• Close the file
  fout.close();

• Read from a file
  std::ifstream fin(filename.c_str());
  if (!fin) // check if opened correctly
  {
    std::cout << "error: open file for input failed!"
    << std::endl;
    exit(127);
  }
  std::string line;
  while ( std::getline (fin,line) ) { // and other methods..
    std::cout << line << std::endl;
  }
  fin.close();

---

**Immagini estratte:**

![Figura estratta 1](images/p35_img01.jpg)


---

<!-- Pagina 36 -->

String streams

• The `<sstream>` header defines streams to and from a string
  • istringstream to read from a std::string
  • ostringstream to write to a std::string
  • stringstream to do both

• They can be used to create strings – for example, when looping

```cpp
std::stringstream ss {};
std::vector< std::string > studentNames {“john”, “jane”};
for(auto student : studentNames)
{
    ss << student << ",";
}
// create a std::string and output to terminal
std::cout << ss.str() << std::endl;
```

• C++ has also the operator+ for strings, but it is not as efficient as a stream

---

**Immagini estratte:**

![Figura estratta 1](images/p36_img01.jpg)
