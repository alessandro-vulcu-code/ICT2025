## Introduction to Programming in Spark

### Functional Programming

While most concepts explained in this section are general, the syntax and the examples will be given in Java. Things in Python are rather similar and you can read the details here (click on the Python stub.)

One of the core ideas of functional programming is that functions can be arguments to other functions. For instance, a function implementing a sorting algorithm may take as a parameter the comparison function along with the data to be sorted. Java 8 introduced support for this style of programming by adding new syntax for specifying so-called anonymous functions, also called lambdas. This syntax allows to write functions directly in the argument list of other functions. The syntax for specifying a function is the following:

Java

```
(T1 param1, T2, param2, ...) -> {
  // Body of the function with as many statements as you need
  // separated by semicolons, just like regular Java statements.
  return /* possibly something */; 
}
```

where **T1** and **T2** are the types of **param1** and **param2**, respectively. If the function is made by a single statement, a more concise syntax can be used:

`(T1 param1, T2 param2) -> /* single statement with no semicolon */`

the result of the single statement will be the return value of the function. If the type of the parameters can be inferred from the context, it can be omitted. An example will make things clearer.

Imagine you have a collection `coll` of `Double` with a method `map` (more on such collections later). The `map` method transforms the collection into a new one by applying the function passed as a parameter to each element. Therefore, to obtain a collection of the squared values you should do the following:

`coll.map((Double x) -> x*x);`

Since the collection is of `Double`, the compiler can infer the type of `x`, so in this case we can write:

`coll.map((x) -> x*x);`

To make another example, imagine that you want to transform your collection of `Double` into a collection of differences from some other value, defined in a variable:

Java

```
double fixed = 1.5;
coll.map((x) -> {
  double diff = fixed - x;
  return diff;
});
```

Note that `fixed` is used in the body of the anonymous function, but is defined outside of it! In such cases we say that the anonymous function **captures** a variable. You cannot re-assign a captured variable within an anonymous function. Trying to do it will result in a compilation error mentioning that all captured variables must be **effectively final**, which is the compiler’s way of saying that you cannot re-assign them.

Java 8 also introduced another way of passing functions to other functions, namely **method references**. Suppose you have the following class:

Java

```
public class Operations {
  public static double square(double x) {
    return x * x;
  }
}
```

You may pass the static method `square` to the method `map` instead of defining a lambda function, like in the examples above. The syntax to refer the static method `square` is the following:

`coll.map(Operations::square);`

note the double colon joining the method name `square` to the class it belongs to, `Operations`. Therefore, you have two ways of passing a function to a method: either you pass an anonymous function or a method reference. Usually, lambda functions are used when the functionality can be coded in a few statements and is limited to a single occurrence. Method references, on the other hand, are useful when the code gets more complex or when it should be reused in several places.

---

## Mini-guide to Spark implementation of MapReduce algorithms

Below we give a brief description of the most relevant Spark features and methods which can be used for the implementation of MapReduce algorithms. The presentation refers to Java as a default, reporting main differences with Python, when needed. For minor differences with Python (e.g., in the syntax), refer to the official Spark Python API.

### Configuration

First, let us look at the basic settings required in your program to use Spark, which were already present in the template provided for Homework 1. The entry point to Spark is the **Spark context**. Since Spark can run on your laptop as well as on many different cluster architectures, to simplify the user experience Spark developers have created a single entry point that handles all the gory details behind the scenes. To create the context you first need to provide some configuration using:

Java

```
SparkConf configuration =
  new SparkConf(true)
    .setAppName("application name here")
```

Let’s break down the code snippet above. We pass `true` to the `SparkConf` constructor. This has the effect that configuration properties can also be passed on the command line. Alternatively, they must be set invoking suitable methods from the `SparkConf` object being created. For example, the code above sets the name of the application in this fashion.

There is a configuration property, the **master**, which is important to ensure the correct execution of a program. This can be set by invoking method `.setMaster(master-address)` after the `.setAppName` method from the `SparkConf` object being created (although for this course you do not need to use this method as explained below). As detailed in the Spark documentation, there are several values that the master address can take. For example:

- **"local[*]"**: uses the local resources of the computer. This sets up a Spark process on the local machine, using the available cores for parallelism. This master address must be used when testing code on your local machine. However, Python users do not need to explicitly set this master, since it is the default, while for Java users it is convenient to set the master using the VM options in the Intellij interface, rather than using the aforementioned `setMaster` method. This choice gives the flexibility of running the code on different architectures.
    
- **"yarn"**: runs Spark on the Yarn cluster manager. This is the cluster manager used by the cluster available for the course. However, take notice that when you run the code on the cluster through the `spark-submit` command that we instruct you to use, the master is automatically set to yarn, so you do not need to explicitly do the setting. Just make sure, in this case, that you are not accidentally setting it to `local[*]`.
    

Based on the configuration object `conf` created above, the Spark context is instantiated as follows:

`JavaSparkContext sc = new JavaSparkContext(conf);`

### Reading from a file

A way (but not the only one!) to read an input dataset is to store the dataset as a text file, located at some path `filepath` which is passed as input to the program, and then load the file into an RDD of strings, with each string corresponding to a distinct line in the file:

`JavaRDD<String> lines = sc.textFile("filepath");`

The `filepath` can be substituted with `args[0]`, if it is passed as the first parameter on the command line. Note that if a path to a directory rather than to a file is passed to `textFile`, it will load all files found in the directory into the RDD.

### Key-value pairs

**For Java users.** In Java, a dataset of key-value pairs with keys of type **K** and values of type **V** is implemented through a `JavaPairRDD<K,V>` object, which is an RDD whose elements are instances of the class `Tuple2<K,V>` (from the Scala standard library). Given a pair `T`, instance of `Tuple2<K,V>`, the methods `T._1()` and `T._2()` return the key and the value of the pair, respectively.

**For Python users.** In Python, a dataset of key-value pairs can be implemented as a simple RDD whose elements are built-in Python tuples.

More on RDDs of key-value pairs in Spark (both for Java and Python users) can be found here.

### Map phase

In order to implement a map phase where each key-value pair, individually, is transformed into 0, 1 or more key-value pairs, the following methods can be invoked from an instance **X** of `JavaPairRDD<K,V>`:

- **mapToPair(f).** (The method can also be invoked from a `JavaRDD<T>` object.) It applies function `f` passed as a parameter to each individual key-value pair of **X**, transforming it into a key-value pair of type `Tuple2<K',V'>` (with arbitrary **K'** and **V'**). The result is a `JavaPairRDD<K',V'>`. Note that the method cannot be used to eliminate elements of **X**, and the returned RDD has the same number of elements as **X**. To filter out some elements from **X**, one can invoke either the `filter` or the `flatMapToPair` methods described below.
    
- **flatMapToPair(f).** It applies function `f` passed as a parameter to each individual key-value pair of **X**, transforming it into 0, 1 or more key-value pairs of type `Tuple2<K',V'>` (with arbitrary **K'** and **V'**), which are returned as an iterator. The result is a `JavaPairRDD<K',V'>`. (The method can also be invoked from a `JavaRDD<T>` object.)
    
- **mapValues(f).** It transforms each key-value pair `(k,v)` in **X** into a key-value pair `(k,v'=f(v))` of type `Tuple2<K,V'>` (with arbitrary **V'**) where `f` is the function passed as a parameter. The result is a `JavaPairRDD<K,V'>`.
    
- **flatMapValues(f).** It transforms each key-value pair `(k,v)` in **X** into multiple key-value pairs `(k,w_1), (k,w_2) , ...` of type `Tuple2<K,V'>` (with arbitrary **V'**). The `w_i`'s are returned as an `Iterable<V'>` by `f(v)`, where `f` is the function passed as a parameter. The result is a `JavaPairRDD<K,V'>`.
    

### Reduce phase

In order to implement a reduce phase where each set of key-value pairs with the same key are transformed into a set of 0, 1 or more key-value pairs, the following methods can be invoked from a `JavaPairRDD<K,V>` object **X**:

- **groupByKey().** For each key `k` occurring in **X**, it creates a key-value pair `(k,w)` where `w` is an `Iterable<V>` containing all values of the key-value pairs with key `k` in **X**. The result is a `JavaPairRDD<K,Iterable<V>>`. The reduce phase of MapReduce can be implemented by applying `flatMapToPair` after `groupByKey`.
    
- **groupBy(f).** It applies function `f` passed as a parameter to assign a key to each element of **X**. Then, for each assigned key `k` creates a key-value pair `(k,w)` where `w` is an `Iterable<K,V>` containing all elements of **X** that have been assigned key `k`. The result is a `JavaPairRDD<H,Iterable<K,V>>`, where **H** is the domain of the keys assigned by `f`. The partitions induced by `f` can then be processed individually by applying a method such a `flatMap` or `flatMapToPair` to the RDD resulting from `groupBy`.
    
- **reduceByKey(f).** For each key `k` occurring in **X**, it creates a key-value pair `(k,v)` where `v` is obtained by aggregating all values of the key-value pairs with key `k` through the function `f` passed as a parameter. For example, if `f` is specified as `(x,y)->x+y`, then `v` will be the sum of all values of the key-value pairs with key `k`. The aggregation is performed efficiently exploiting the partitions of the RDD **X** created by Spark (perhaps as a consequence of the invocation of the `repartition` method): first the values are aggregated within each partition, and then across partitions. The result is a `JavaPairRDD<K,V>`.
    

**For Python users.** All of the above methods have a Python equivalent with the same name, except for `mapToPair` and `flatMapToPair` which, in Python, become `map` and `flatMap`. Some transformations, however, require that the elements of the RDD be key-value pairs.

### Partitioning

An RDD is subdivided into a configurable number of partitions, which may be distributed across many machines. For transformations acting on individual elements of an RDD (e.g., those listed above to implement the Map phase of a MapReduce round), Spark defines a number of tasks equal to the number of partitions. Each task corresponds to the application of the given transformation to the elements of a distinct partition. Also, in Spark each machine is called an **executor**, and may have many cores. Each task will be assigned to a core for execution. A higher number of partitions allows for better exploitation of the available cores, better load balancing and smaller local space usage. However, managing too many partitions may eventually introduce a large overhead.

The number of partitions, say `num-part`, can be set by invoking the `repartition(num-part)` method. In this case, the elements of the RDD are randomly shuffled among the partitions and this is a way to attain a random partitioning.

> **Important:** since RDDs are immutable, the number of partitions can be set only when the RDD is first defined.

Let **X, Y, Z** be RDD variables and consider the following sequence of 3 instructions:

Java

```
Y = X.repartition(4) 
Y.repartition(8) 
Z = Y.repartition(8)
```

After the 3 instructions have been executed, **Y** is subdivided into 4 partitions (the second instruction has no effect on its partitioning) and **Z** is subdivided into 8 partitions.

The number of partitions can also be passed as input to the `textFile` method described above (e.g., `JavaRDD<String> docs = sc.textFile("filepath", num-part)`), but in this latter case it is regarded as a "minimum" number of partitions and also the achieved partition is not necessarily random.

Let **X** be an RDD containing objects of type **T**, partitioned into **p** partitions. The following methods allow you to gather and work separately on each partition:

- **mapPartitions(f) and mapPartitionsToPair(f).** They apply function `f` passed as a parameter to the elements of each partition, which are assumed to be provided as an iterator. Function `f` must return 0, 1 or more objects of some type **T'**. Hence, the result is a `JavaRDD` of elements of type **T'**. If `mapPartitionsToPair` is used, then type **T'** must be `Tuple2<K',V'>` and the result is a `JavaPairRDD<K',V'>`.
    
- **glom().** (the name says it all :-). It returns an RDD whose elements are arrays (Java) or lists (Python) of objects of type **T**, and each such array/list contains the objects of a distinct partition of **X**. The partitions can then be processed individually by applying a method such a `flatMap` or `flatMapToPair`, with a suitable function, to the RDD resulting from `glom`.
    

**For Python users.** All of the above methods have a Python equivalent with the same name, except for `mapPartitionsToPair` which does not exist in the Python API.

### Additional useful methods

The following methods can be invoked from an RDD **X** of elements of type **T**:

- **count().** An action that returns the number of elements in **X**.
    
- **map(f).** A transformation that applies function `f` to each individual element **X**. Function `f` accepts a single input of type **T** and returns an output of type **R**.
    
    - _Example:_ `JavaRDD<Double> halves = numbers.map((x) -> x / 2.0);`
        
- **reduce(f).** An action that returns a single value of type **T** by combining all the values of the RDD according to function `f`, which must be associative and commutative.
    
    - _Example:_ `int sum = numbers.reduce((x, y) -> x + y);`
        
    - **Important:** this method should not be confused with the Reduce Phase in MapReduce. They are rather different things!
        
- **filter(f).** A transformation that returns an RDD containing only the elements in **X** for which `f` returns true.
    
    - _Example:_ `JavaRDD<Double> evenNumbers = numbers.filter((x) -> x % 2 == 0);`
        
- **countByValue().** An action that returns a Map/Dictionary that for each element `e` in the RDD **X** contains an entry `(e, count(e))`.
    
- **sortByKey(ascending).** A transformation that can be applied when the elements of **X** are key-value pairs. sorts the elements of **X** by key in increasing order (`true`) or decreasing order (`false`).
    
- **collect().** An action that brings all the data contained in **X** into a list stored on the driver.
    
    - **Warning:** this action needs enough memory on the driver to store all data in **X**, otherwise an `OutOfMemoryError` will be thrown.
        
- **take(num).** An action that brings the first `num` elements of **X** into a list stored on the driver.
    
- **min(comp), max(comp).** Actions that return the minimum/maximum element in **X**.
    
    - **Java users:** The argument `comp` must implement `Comparator` and `Serializable`.
        
    - **Python users:** The argument `comp` is optional.
        

### Shared variables

Sometimes, read-only global data must be used by RDD transformations. If a variable `Var` is assigned only once, Spark creates a copy for each task. For large structures, use **broadcast variables**:

- Java: `Broadcast<T> sharedVar = sc.broadcast(Var)`
    
- Python: `sharedVar = sc.broadcast(Var)`
    

Access value via `sharedVar.value()` (Java) or `sharedVar.value` (Python).

**Accumulators** are special shared variables that can only be modified through associative and commutative operators (like additions).

### Profiling

#### Time measurements

In Java, use `System.currentTimeMillis()`. However, because Spark transformations are **lazy**, they only execute when an action is called. To measure specific code without including file loading time, you should **cache** the RDD and force an action:

Java

```
JavaRDD<String> docs = sc.textFile("filepath").cache();
numdocs = docs.count();
long start = System.currentTimeMillis();
// Code to measure
long end = System.currentTimeMillis();
```

#### Web interface

- **Local mode:** Access `localhost:4040` while the program is running. Insert `System.in.read();` at the end of `main` to keep the process alive.
    
- **On the cluster:** Visit `http://147.162.226.106:18080/` (Unipd network only) to see the History Server for executed applications.
    

### Official and additional documentation

- Apache Spark Site
    
- **For Java users:** RDD Programming guide, JavaRDD and JavaPairRDD API.
    
- **For Python users:** RDD Programming guide, RDD Python API.
    

_Last update: 19/05/2023_