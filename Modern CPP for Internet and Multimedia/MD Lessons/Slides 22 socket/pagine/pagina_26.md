TCP listen

• TCP is a connected protocol, the **server** uses the bound socket as a listen socket to accept connection
• After creating and binding the listener socket **scklist**, the listen method is called to set how many client can be accepted together

```javascript
if (listen(scklist, 5) < 0) { // Accept max
  5 clients together
  //ERR
}
```

• In these basic examples we will always serve one client at a time
• To serve more clients you need multithreading.. We’ll see it next time

---

**Immagini estratte:**

![Figura estratta 1](images/p26_img01.jpg)
