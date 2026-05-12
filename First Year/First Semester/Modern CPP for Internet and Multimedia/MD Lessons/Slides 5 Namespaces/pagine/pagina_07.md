Access to namespace members

• using directives

using namespace std;

string a_string {"hello"};
vector<string> vec {a_string}
// instead of std::string a_string
// and std::vector<std::string> vec

Use them with care

• They may lead to the same name clashes that namespaces were introduced to avoid

• Don’t place them in the global scope of an header file (which could be #included anywhere)

---

**Immagini estratte:**

![Figura estratta 1](p07_img01.jpg)
