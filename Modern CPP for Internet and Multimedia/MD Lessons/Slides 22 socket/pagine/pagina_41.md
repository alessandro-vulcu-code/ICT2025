TCP server example – listen and accept

if (listen(scklist, 5) < 0) { // Accept max 5 clients together
    //ERR
}

struct sockaddr_in client_addr;

socklen_t addr_l = sizeof(client_addr);

int sockfd = accept(scklist, (struct sockaddr*) &client_addr, &addr_l);

if(sockfd < 0) {
    /*ERROR! CLOSE AND EXIT*/
}

std::cout << " connection from " << inet_ntoa(client_addr.sin_addr);

---

**Immagini estratte:**

![Figura estratta 1](images/p41_img01.jpg)
