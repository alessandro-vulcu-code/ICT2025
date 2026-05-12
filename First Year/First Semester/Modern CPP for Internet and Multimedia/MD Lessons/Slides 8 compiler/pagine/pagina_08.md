Preprocessor: Conditional compilation

```cpp
//my-fun.h
#ifndef MY_FUN_H
#define MY_FUN_H
inline int incr(int i)
{
    return i+1;
}
#endif

If MY_FUN_H already been defined, do not compile this code

• This construct is the wrapper #ifndef or “include guards”
• When the header is included again, the conditional will be false, and the preprocessor will skip over the entire contents of the file, and the compiler will not see it twice.
• Always use it in all your .h files: you never know if you need to include them somewhere in the future!!
• Be sure all headers are defined with a different name, or you’ll have big troubles!!!
```

---

**Immagini estratte:**

![Figura estratta 1](p08_img01.jpg)
