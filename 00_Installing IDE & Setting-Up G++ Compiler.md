# Install any IDE that you like: 
- I am a windows user, & I love using VS Code 


## What is an IDE (Integrated Development Environment): 

- An Integrated Development Environment (IDE) is a software application that provides comprehensive facilities to computer programmers for software development. 

- An IDE typically consists of:

    1. `Source Code Editor:` 
        A text editor that provides syntax highlighting, code completion, and other features to facilitate writing code.
    
    2. `Compiler/Interpreter:` 
        Tools to convert the written code into executable programs.
    
    3. `Debugger:` 
        A tool to test and debug programs by allowing developers to run the code step-by-step, inspect variables, and track the control flow.
    
    4. `Build Automation Tools:` 
        Tools to automate tasks like compiling the code, packaging the binaries, running tests, and deploying the application.
    
    5. `Version Control Integration:` 
        Support for version control systems like Git, allowing developers to manage and track changes to the source code.
    
    6. `Project Management Features:` 
        Tools to manage files, resources, and dependencies within a project.
    
    7. `Graphical User Interface (GUI):` 
        A user-friendly interface to interact with the various components of the IDE.

- Popular examples of IDEs include `Visual Studio Code`, `Eclipse`, `IntelliJ IDEA`, and `Xcode`. They help streamline the development process by integrating multiple development tools into a single application, enhancing productivity and efficiency.


# Install MinGW "g++" compiler: 
- It will help us in compiling our C++ code files 


## For Installing "g++" compiler in Windows 10: 

- Go to "mingw-w64.org" 
- Go to "Downloads" 
- In "Pre-built toolchains and packages" section, inside table click on 8th row option "MingW-W64-builds" 
- Now in "Mingw-builds" section click on "Installation: GitHub" 
- Now You will be redirected to a GitHub page 
- Checkout the latest release "Assets" dropdown menu 


### Here in assets you would be able to see a lot of names of the builds like: 

```
i686-13.2.0-release-posix-dwarf-msvcrt-rt_v11-rev0.7z  
i686-13.2.0-release-posix-dwarf-ucrt-rt_v11-rev0.7z  
i686-13.2.0-release-win32-dwarf-msvcrt-rt_v11-rev0.7z  
i686-13.2.0-release-win32-dwarf-ucrt-rt_v11-rev0.7z  
x86_64-13.2.0-release-posix-seh-msvcrt-rt_v11-rev0.7z  
x86_64-13.2.0-release-posix-seh-ucrt-rt_v11-rev0.7z  
x86_64-13.2.0-release-win32-seh-msvcrt-rt_v11-rev0.7z  
x86_64-13.2.0-release-win32-seh-ucrt-rt_v11-rev0.7z  
```

> Choose a build which is compatible with your system 


### Guide for choosing the appropriate build version (If new releases have some new terms introduced in them, just do ChatGPT): 

- These above filenames describe different builds of the GCC compiler, including G++, for various configurations on Windows. Here's a breakdown of these terms:

    1. `Architecture (i686 vs. x86_64):`  
        - i686: 32-bit architecture.
        - x86_64: 64-bit architecture.

    2. `Version (13.2.0):` 
        - The version number of the GCC compiler.

    3. `Release (release):` 
        - Indicates that this is a release version.

    4. `POSIX vs. Win32:`  
        - posix:  
              - Uses POSIX threads, which are typically used for compatibility with Unix-like systems.  
              - posix Indicates that the environment is POSIX-compatible (Portable Operating System Interface), which is a family of standards specified by the IEEE for maintaining compatibility between operating systems.  
        - win32:  
              - Uses Windows-native threads.   

    5. `Exception Handling Model (dwarf vs. seh):`  
        - dwarf: DWARF is a debugging standard and also used here for exception handling.
        - seh: Structured Exception Handling, which is specific to Windows.

    6. `Runtime (msvcrt vs. ucrt):`  
        - msvcrt: Uses the Microsoft C Runtime Library called "Microsoft Visual C++ Runtime Library".
        - ucrt: Uses the Universal C Runtime Library, which is a newer version of the Microsoft C Runtime.

    7. `Runtime Version (rt_v11):`  
        - rt_v11: Indicates the version of the runtime library.
    
    8. `Revision (rev0):`  
        - rev0: The revision number of this particular build.

    9. `File Format (.7z):`  
        - .7z: The file extension indicating that the file is compressed using the 7-Zip format.


### I am Windows user and my PC has a 64-bit architecture that's why I am choosing "x86_64-13.2.0-release-win32-seh-ucrt-rt_v11-rev0.7z" build 

```
    - seh is recommended for 64-bit Windows as it is more efficient and better supported. 
    - ucrt is the newer version and is recommended for modern applications.
```


### Completing Installing G++: 
- Click the build that you have choosen and the build will get downloaded automatically 
- Extract all the files from this downloaded folder 
- Now make a new folder named `MinGW` in your computer's `C-Drive` and cut paste all the extracted files into the MinGW C-drive directory  
- Now in your C-Drive you're in the newly created "MinGW" folder, and in that folder all the folders and files that you have extracted are present, now out of all these folders which are present, go to "bin" folder 
- Copy the path to this `bin` folder 
- Press "Windows" button on your keyboard and search `Edit the system environment variables` 
- Click on `Environment Variables` button, which is present in bottom right corner 
- Now below in `System Variables` section, click on `Path` and then on `Edit` button which is present in botton right corner 
- Here click on "New" Button, paste the copied path here, if MinGW bin path is on the top then move it below the system paths and then press "Ok, ok & ok" and close all the tabs of this "Edit the system environment variables" section 
- Now you have successffuly installed the "g++" compiler 
- To check whether it is successfully installed or not, open `Command Prompt` and type this command: `g++ --version` 
- If you have done all the steps correctly and if your "g++" compiler is installed successfully then this command will tell you the version of the "g++" compiler that you have installed in your PC 


### Response of "g++ --version" command in My PC's Command Prompt: 

```
g++ (x86_64-win32-seh-rev0, Built by MinGW-Builds project) 13.2.0  
Copyright (C) 2023 Free Software Foundation, Inc.  
This is free software; see the source for copying conditions.  There is NO  
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  
```


### Just do ChatGPT or StackOverflow if you're facing any error while installation 


> If you're using VS Code, don't forget to download C/C++ intellisense extension for support 

_ _ _ 


# What is MinGW: 

- MinGW (Minimalist GNU for Windows) is a minimalist development environment for native Microsoft Windows applications. It includes a set of programming tools that allow you to compile and build native Windows applications using the GCC (GNU Compiler Collection), which includes the G++ compiler for C++.


# What Things Do you Get in a MinGW Build: 

- When you download the MinGW build binary of x86_64-13.2.0-release-win32-seh-ucrt-rt_v11-rev0.7z, you get a collection of tools, not just the G++ compiler. Here's what you typically get:

    ### GCC (GNU Compiler Collection):
      1. G++: The C++ compiler.
      2. GCC: The C compiler.
      3. GFortran: The Fortran compiler.
      4. GCJ: The Java compiler (optional and less commonly used).
      
    ### Binutils:
      - Tools for assembling, linking, and managing binaries, such as as (assembler), ld (linker), and ar (archiver). 
      
    ### GNU Debugger (GDB):
      - A powerful debugging tool to debug your applications. 

    ### Make: 
      - A build automation tool to manage project builds.

    ### Libs: 
      - Standard libraries such as the C standard library (libc), C++ standard library (libstdc++), and others.
    
    ### MSYS2 (Minimal SYStem 2):
      - A collection of Unix-like tools for Windows, providing a POSIX-compatible environment for running shell scripts and utilities (though this may need to be downloaded separately depending on the distribution).