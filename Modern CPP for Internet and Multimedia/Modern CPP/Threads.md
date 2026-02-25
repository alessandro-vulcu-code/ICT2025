# Metodi di Creazione dei Thread in C++

In C++ moderno (C++11 e successivi), la libreria standard `<thread>` offre diversi modi flessibili per avviare l'esecuzione parallela. Ecco una panoramica dei metodi principali, dai più classici ai più moderni.

## 1. Puntatore a Funzione

Il modo più semplice e basilare: si passa il nome di una funzione globale o statica al costruttore di `std::thread`.

```cpp
#include <iostream>
#include <thread>

void task() {
    std::cout << "Esecuzione da funzione globale\n";
}

void task_with_arg(int x) {
    std::cout << "Argomento ricevuto: " << x << "\n";
}

int main() {
    std::thread t1(task);
    std::thread t2(task_with_arg, 42); // Passaggio di argomenti

    t1.join();
    t2.join();
    return 0;
}
```

## 2. Espressione Lambda

Molto comune nel C++ moderno per compiti brevi e locali. Permette di definire la logica del thread direttamente nel punto di creazione e di catturare variabili dal contesto circostante.

```cpp
#include <iostream>
#include <thread>

int main() {
    int value = 10;

    // Lambda che cattura 'value' per riferimento
    std::thread t([&value]() {
        value += 5;
        std::cout << "Valore nella lambda: " << value << "\n";
    });

    t.join();
    return 0;
}
```

## 3. Oggetto Funzione (Functor)

Si passa un'istanza di una classe che ha l'operatore di chiamata di funzione `operator()` sovraccaricato. È utile quando il thread deve mantenere uno stato interno complesso.

```cpp
#include <iostream>
#include <thread>

class Worker {
public:
    void operator()() {
        std::cout << "Esecuzione da Functor\n";
    }
};

int main() {
    std::thread t((Worker())); 
    // Nota: le doppie parentesi servono per evitare il 
    // "Most Vexing Parse" del C++, oppure si usa l'inizializzazione uniforme:
    // std::thread t{Worker()};

    t.join();
    return 0;
}
```

## 4. Funzione Membro (Metodo di una Classe)

Per eseguire un metodo di un oggetto specifico in un thread separato. Richiede di passare:
1. Il puntatore al metodo (`&Classe::Metodo`).
2. Il puntatore all'oggetto su cui chiamarlo (`this` o `&oggetto`).
3. Eventuali argomenti del metodo.

```cpp
#include <iostream>
#include <thread>

class Calculator {
public:
    void add(int a, int b) {
        std::cout << "Somma: " << (a + b) << "\n";
    }
};

int main() {
    Calculator calc;
    
    // Esegue calc.add(10, 20) in un thread separato
    std::thread t(&Calculator::add, &calc, 10, 20);

    t.join();
    return 0;
}
```

## 5. Funzione Membro Statica

Simile alle funzioni globali, ma incapsulate dentro una classe. Non richiedono un'istanza dell'oggetto.

```cpp
#include <iostream>
#include <thread>

class Logger {
public:
    static void log(const std::string& msg) {
        std::cout << "[LOG]: " << msg << "\n";
    }
};

int main() {
    std::thread t(&Logger::log, "Messaggio statico");
    t.join();
    return 0;
}
```

## 6. `std::jthread` (C++20)

Introdotto in C++20, `std::jthread` ("joining thread") è un miglioramento di `std::thread`.
- **Join automatico**: Non serve chiamare `.join()` esplicitamente; il distruttore lo fa in automatico se il thread è ancora in esecuzione.
- **Supporto stop token**: Facilita la richiesta di interruzione cooperativa del thread.

```cpp
#include <iostream>
#include <thread> // Include jthread in C++20

void task() {
    std::cout << "Esecuzione su jthread\n";
} // t viene joinato automaticamente qui

int main() {
    std::jthread t(task);
    // Non serve t.join()
    return 0;
}
```

## Riassunto

| Metodo | Caso d'Uso Tipico |
| :--- | :--- |
| **Puntatore a Funzione** | Compiti semplici, codice legacy C-style. |
| **Lambda** | Codice conciso, usa-e-getta, necessità di catturare variabili locali. |
| **Functor** | Compiti complessi che richiedono stato interno persistente. |
| **Funzione Membro** | Esecuzione di logica legata a un oggetto specifico (OOP). |
| **`std::jthread`** | (C++20) Preferibile sempre se disponibile per sicurezza (RAII). |
