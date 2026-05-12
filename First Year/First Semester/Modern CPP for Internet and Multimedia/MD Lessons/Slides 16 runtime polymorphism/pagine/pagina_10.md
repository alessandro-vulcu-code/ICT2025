Multiple inheritance

dynamic_cast returns nullptr in case of multiple inheritance

- there is only one component class, but both rx and tx inherit from it
- both the tx and rx will have a base object of type component

- a conversion from radio to storable is ok
- a conversion from radio to component is not ok, as radio has two component subobjects

---

**Immagini estratte:**

![Figura estratta 1](images/p10_img01.jpg)
