# 5 Min Questions

PDF analizzati nella cartella: 35.

Sono state trovate slide con diciture equivalenti a "5 min questions":

- "5 min. question"
- "5 min questions"
- "5 minutes questions"
- "5 minutes question"

## Domande dalle slide

### Slides 10 lab1.pdf - pagina 3

- We want to pass a string `s`, an integer `i` and a double `d` as input parameter to a function. They cannot be modified by the function, and the function should be efficient. How do we pass them?

```cpp
void fun(... s, ... i, ... d);
```

### Slides 15 lab2.pdf - pagina 3

- Please, tell me the difference between:

```cpp
void fun(const std::string* s);
```

and:

```cpp
void fun(std::string* const s);
```

Suggestion from slide: read it right-to-left.

### Slides 20 smart pointers.pdf - pagina 3

- What is an lvalue?
- What is an rvalue?

### Slides 21 lab 4.pdf - pagina 3

- When should I use `unique_ptr`, `shared_ptr` and `weak_ptr`?
- How do I pass a `unique_ptr` to functions?
- How do I use a `weak_ptr`?

### Slide 25 Lab 6.pdf - pagina 3

- What's going on when multiple threads are running in parallel?

### Slide 27 - lab 7.pdf - pagina 3

- What is a race condition?

## Extra da Q&A.pdf

`Q&A.pdf`, pagina 13, non e' una slide intitolata "5 min questions", ma specifica che le 5 minute questions presenti nelle slide sono possibili domande per l'esame teorico/orale e aggiunge queste altre domande:

- Explain which is the role of preprocessor, compiler and linker.
- After the operations below, which is the value of `c`?

```cpp
uint_fast8_t a = 21;
uint_fast8_t b = 11;
uint_fast8_t c = a ^ b;
```

- What happens if two or more threads access a critical region without any thread safe mechanism?
- What is a reference? Provide an example.
- Explain how the switch-case statement works, providing an example.
