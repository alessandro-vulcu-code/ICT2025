File streams

• Write to a file
  fout << "a line" << std::endl
  fout << "another line" << std::endl

• Close the file
  fout.close();

• Read from a file
  std::ifstream fin(filename.c_str());
  if (!fin) // check if opened correctly
  {
    std::cout << "error: open file for input failed!"
    << std::endl;
    exit(127);
  }
  std::string line;
  while ( std::getline (fin,line) ) { // and other methods..
    std::cout << line << std::endl;
  }
  fin.close();

---

**Immagini estratte:**

![Figura estratta 1](images/p35_img01.jpg)
