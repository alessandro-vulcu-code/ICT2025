Lambda function

• Def: a Lambda function (or lambda expression, or lambda) is a simplified notation for defining and using an anonymous function object.
  • It is used whenever you need to call a simple function that you will use like a local variable, so doesn’t make sense to create a function for it

• A lambda is an object of type `std::function<Return(Args)>`
  • Return is the return type
  • Args is the list of parameters

• Some examples:
  • `const std::function<void(int)>`
  • `const std::function<int(int,double)>`

---

**Immagini estratte:**

![Figura estratta 1](images/p27_img01.jpg)
