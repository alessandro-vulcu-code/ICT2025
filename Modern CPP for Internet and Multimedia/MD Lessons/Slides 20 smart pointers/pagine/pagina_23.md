Weak Pointer

• It refers to an object managed by a shared_ptr
  shared_ptr<T1> sp = make_shared<T1>();
  weak_ptr<T1> wp1 = sp1;

• It does not take the ownership of a pointer
• It does not perform any automatic delete to the pointer
• You cannot perform any delete to the pointer with a weak pointer: this is the main difference it has with a raw pointer
• You cannot use → operator directly, to do that you first need to call the function lock()

---

**Immagini estratte:**

![Figura estratta 1](images/p23_img01.jpg)
