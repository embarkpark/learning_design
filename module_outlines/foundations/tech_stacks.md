# Tech stack concepts 1

### Libraries and frameworks

* A library is code that your code calls, 
* ... whereas a framework is code that calls your code.
* Both libraries and frameworks are ways to reuse 3rd-party code.
* Reusing high-quality code is a great way to increase maintainability.
* Because frameworks call you + force you to use their components, they can enforce best-practice patterns for development.
	* Using best-practice patterns is a great way to increase maintainability.

### Libraries, frameworks and platforms

* A library is code that your code calls, 
* A framework is code that calls your code.
* ... whereas a "platform" is a foundational layer that _hosts_ your code for execution.
	* Think: my code is inside an execution container that connects my code to external resources.
	* A platform is not just code that calls your code, like a framework does.
	* Rather, a platform _runs_ your code at a low level, often directly aware of the hardware and interacting with the operating system directly.
* These terms are a little fuzzy
	* The term "platform" is "overloaded" by marketing departments of software companies to mean various things
	* ... but let's use this meaning here.

### CPU architecture

* Every computer has a CPU at its heart.
* A CPU runs very small instructions, like...
	* `ADD` - add two numbers
	* `MOV` - move a small amount of data
	* etc
* Instructions are also called "operations".	
	* So these instructions are called "opcodes", short for "operation codes".
* There are two competing CPU architectures in common use:
	* x86
	* ARM
* x86 is _generally_ used in desktops and servers.
* ARM is _generally_ used in mobile phones.
	* Although recent Apple laptops now use chips based on ARM
* Programs are compiled to machine code that _targets_ one of these architectures.
* A program compiled into machine code is stored as a "binary file", or "a binary".
	* This is also called an "executable".
* CPU instructions are very different x86 and ARM.
	* You cannot execute a program compiled into machine code for the wrong architecture.
	* Another way to say this: "Executables only execute on the target architecture."

### Operating systems

* An operating system is a collection of administrative programs that provide safe, efficient access to the computer's resources.
* Operating systems help programs access and share:
	* CPU time
	* memory
	* long-term storage
	* network access
	* the graphical interface
	* peripherals like the keyboard and trackpad
	* etc
* Like all programs, operating systems are compiled to target a specific CPU architecture.

### CPU architecture, operating systems, and virtual machines

* There are many devices with different architectures.
* You cannot execute a program compiled into machine code for the wrong architecture.
* Thus, by default, you have to have the right executable.
* For convenience of distributing your apps, it's desirable to support many devices with one executable.
* How to do this?
* A "virtual machine" presents one "virtual" architecture on top of multiple real (hardware) architectures.
	* "Virtual machine" is often shortened to "VM".
* Programs written in a language that supports a VM will be compiled to the opcodes for that VM.
	* A program compiled into these VM opcodes is usually called "bytecode".
* Programs that are compiled to the bytecode for a VM will run on any real architecture (i.e., on any actual device) that that VM supports.
* For example, Java programs compiled to the Java VM. The Java VM supports [many operating systems](https://www.java.com/en/download/help/sysreq.html)

### Android, iOS, Dart and Flutter

* Android is a mobile computing _platform_.
	* Android apps run on the Android virtual machine (called "ART"), which then connects with the actual device hardware.
* iOS is a mobile computing _platform_.
	* iOS apps run only on Apple hardware, so they don't need a virtual machine.
* Dart is a _language_ that lets you access the services of the Android and iOS platforms.
	* Dart compiles to native x86 or ARM code for Android and iOS devices.
* Flutter is a _framework_ that lets you write applications in the Dart _language_ to access most of the native services of the Android or iOS _platforms_.
