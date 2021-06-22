# Multiple-dispatch
   **group name**: oh my nunu     
   **list of group members**: Xin, Wang、Qianwen, Yu   
   **laboratory work number**: 3  
   **variant description**: Multiple-dispatch  
# Synopsis
   **Use python to develop a library to implement Multiple-dispatch, which must meet the following conditions:** 

   1. The library should support multiple-dispatch on positional, optional, and named arguments.
   2. Your library should be well documented.
   3. To prove correctness, you should use unit tests with several multi-methods, which work
      with standard Python types and user-defined types. 
   4. You should demonstrate how it works with inheritances and multiple inheritances.
   5. It will be preferred if you design a complex real-world example.
   6. Do not forget about before, after, and aroung modifications. See Common Lisp
      documentation for that (https://lispcookbook.github.io/cl-cookbook/clos.html#
      method-qualifiers-before-after-around).   

   **To implement this lab,which must to do:**  

   1. Write a decorator that implements polymorphism in a function.   
   2. Scan a function's arguments to determine if they belong to an instance of an entry of type in TypeMap, and if so, return the function corresponding to that entry.
   3. Using decorators, the arguments of a child class are recognized by the function as arguments of the parent class.

     

# Contribution summary for each group member
   **Qianyu, Wen(github: yqw123)**: Complete the multi_dispatch.Finish part of the report.   
   **Xin, Wang(github: zhanglangEB)**:  Complete the methods the tests of methods.Finish part of the report.


# Work demonstration 
   1. multimethod  

      ```
      def register(function):
        function = getattr(function, "__lastreg__", function)
        name = function.__name__
        mm = registry.get(name)
        if mm is None:
            mm = registry[name] = MultiMethod(name)
        mm.register(types, function)
        mm.__lastreg__ = function
        return mm
	  return register
      ```

   2. foo(typename1,typename2)  

      ```
      @multimethod(typename1,typename2)
	  def foo(a, b):
		return a + b
      ```

   3. foo(classname1,classname2)  

      ```
      @multimethod(classname1,classname2)
	  def foo(a, b):
		print(type(a), type(b))
		return 'classname1'+'classname2'
      ```
   
	

	  
	


# Conclusion

  multimethods:a function that has multiple versions, distinguished by the type of the arguments.
  
  So what could this look like using multimethod dispatch? Decorators are a good match:
  
  there's a global registry indexed by function name ('foo' in this case), 
  
  pointing to a registry indexed by tuples of type objects corresponding to the arguments passed to the decorator.
  
  
