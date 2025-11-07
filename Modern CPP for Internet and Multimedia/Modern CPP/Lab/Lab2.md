## 💻 Modern C++ Programming for ICT

### Pagina 2

Modern C++ Programming for ICT
Outline
1. Class Packet: c-style array, array or vectors?
2. Let's be sure we have up to one header per layer: map

---

### Pagina 3
### Class Packet
The class Packet (examples/print_headers/)
Create the class Packet that must have:
- **Private:**
    - `headers`: a list of `Header` pointers heap-allocated (with `new`) by the calling function (e.g., the `main`).
    - `hdr_counter`: counter of headers inserted to the packet so far.
- **Public:**
    - `Constructor`
    - `void addHeader(Header* p);`: it adds `p` to `headers`, if `p` is not `nullptr`, and increments the value of `hdr_counter`.
    - `getNumHeaders() const`: that returns the number of added headers.
    - `Destructor`, that removes and deletes all headers.
    - `print()` function that prints to standard output the info of each headers stored in the list (include `iostream` in `packet.cpp`).

---

### Pagina 4

### Class Packet

The class Packet solutions with array
- C-style stack allocated array of pointers to `Header` objects
    C++
```
    Header* headers[7];
    size_t hdr_counter;
``` 
- stack allocated C++ array style of pointers to `Header` objects
    
    C++
    
    ```
    std::array< Header *, 7> headers;
    size_t hdr_counter;
    ```
    
    Both solutions use efficient data structure, but have two drawbacks:
    
- Need of the additional variable `hdr_counter` to keep track about the number of travelers added
    
- Requires knowing the size of the array in advance
    

---

### Pagina 5

### Arrays as object attributes

- You need to set their size when declaring them.
    
- Why? Because the compiler must know the complete size of the object to allocate it into the stack.
    
    - Problem: which size?
        
- You may allocate a heuristic big size, hoping not to overflow.
    
- Problem 1: waste of resources. We are using $C++$ to be efficient, so we don't like this solution
    
- Problem 2: overflow. Maybe you need more space than the one you considered.
    
- Array should be used when you want to efficiently handle data of which you know the max size in advance (e.g., I/O buffers).
    
    Class packet
    

---

### Pagina 6

### Solution with array: manual heap allocation

- Heap allocated (free storage) C-style array of pointers to `Header` objects
    
    C++
    
    ```
    Header** headers;
    size_t hdr_counter;
    ```
    
- In the `Packet` constructor
    
    C++
    
    ```
    Packet(int size) : tot_headers(size) {
        headers = new Header*[size];
    }
    ```
    
- In the `Packet` destructor add
    
    C++
    
    ```
    delete [] headers;
    ```
    

---

### Pagina 7

### Class Packet

The class Packet solution with vector

- C++ standard library gives you the `std::vector`
    
    C++
    
    ```
    std::vector<Header> headers;
    ```
    
- You don't need to know the size in advance
    
- You don't need to use an additional counter variable
    
    C++
    
    ```
    headers.size();
    ```
    
- Why? Because it contains a pointer to heap (or free storage) elements created with new.
    
    It is a wrapper of an array with dynamic size. It has contiguous elements.
    
- Drawback: less efficient than arrays, occupies more space.
    
- You can set the possible max size using the `reserve(size)` method, if you want (you don't need to, but it will be more efficient, without performing resize operations).
    

---

### Pagina 8

### Class Packet

The class Packet solution with vector

C++

```
std::vector<Header>> headers; // Nota: Probabile errore di battitura, dovrebbe essere std::vector<Header*> o std::vector<Header>
```

You can add elements with (more than) two functions

- `insert(pos,element)`
    
- `emplace_back(element);`
    

---

### Pagina 9

### Class Packet

The class Packet: how not to use it

- The following use is wrong!
    
    C++
    
    ```
    main() {
	    Packet pkt();
	    MacHeader mac():
	    Header* p_hdr = &mac;
	    pkt.addHeader(p_hdr);
    }
    // points in memory an object that does not exist in memory, leading to segmentation fault and double deletion
    ```
    
- Why???
    

---

### Pagina 10

### Class Packet

The class Packet: how not to use it - 2

C++

```c++
main() {
	Packet pkt();
	if(/*some conditions*/) {
		MacHeader mac();
		Header* p_hdr = &mac;
		pkt.addHeader(p_hdr);
	}
std::cout << pkt().print(); // prints the content of all headers
}							//stored in the packet
```

- `std::cout` will access a pointer which references to a... _(memoria deallocata o fuori scope)_
    

---

### Pagina 11

### Class Packet

The class Packet: how to use it

C++

```
main() {

}

Packet pckt();

pckt.addHeaders(new MacHeader());
```

- Question: an object has been created with `new`, where and when the object is going to be destroyed with `delete`?
    
- Answer: `Packet` destructor must `delete` each inserted element, as it owns them now.
    

---

### Pagina 12

### The class Packet: destructor

- Sol1: iterators
    
    C++
    
```c++
    Packet::~Packet(){
    
    for(std::vector<Header*>::iterator it = headers.begin();
    
    it ≠ headers.end(); it++) {
    
    delete *it;
    
    }
    
    }
```
    
- Sol2: use `[]`
    
    C++
    
    ```
    Packet::~Packet(){
    
    for(int k=0 ; k < headers.size(); k++) {
    
    delete headers[k];
    
    }
    
    }
    ```
    

---

### Pagina 13

### Class Packet

The class Packet: destructor - 2

- Sol2: element access
    
    C++
    
    ```
    Packet::~Packet(){
    
    for(Headers* p : headers) {
    
    delete p;
    
    }
    
    }
    ```
    

---

### Pagina 14

## Homework

### New specs

NEW SPEC: The position of the header in the array (or in the vector) is the actual layer position of the iso-osi stack

- Inside the class `Header` we need to define:
    
    - scoped enum `OsiLayer = {PHY=1,MAC, NET,TRAN,SESS, PRES,APP};`
        
    - (const) member variable `OsiLayer layer` initialized at the constructor of the `Header` class (change it to `Header (OsiLayer l, int size)`)
        
    - `MacHeader(int size)` will call `Header(OsiLayer::MAC,size)`
        

---

### Pagina 15

## Homework

### New specs - 2

- In the `Packet` class, try to provide a solution using the `std` data structures
    
- E.g., using `std::map<Header:: OsiLayer, Header*> headers;`
    
- Change `addHeader` from `void` to `bool addHeader(Header* p);` that forbids both insertion of null pointers and layers already inserted
    
- No more than one MAC, one TRAN, etc..
    

---

### Pagina 16

## LAB 2-bis

### LAB 2 bis: git

- Just stay in the branch of `lab2` and modify your code there
    
- Push your code at the end with a commit **“lab2 bis”**
    

---

I contenuti sono stati formattati come richiesto.

Vuoi che ti dia qualche suggerimento su come implementare le nuove specifiche dell'Homework, in particolare la logica della funzione `bool addHeader(Header* p)` utilizzando la `std::map`?