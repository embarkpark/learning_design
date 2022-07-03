# Material components

### What is a design system?
* A design system is a collection of color schemes, layouts, typography, animations, components and behaviors that work together to produce a unified effect on the users.
* Because design systems are unified and consistent...
	* ... they improve usability
		* Surprising the user is often an unpleasant surprise.
			* A [popular book](https://www.amazon.com/Dont-Make-Think-Revisited-Usability/dp/0321965515/ref=pd_lpo_1?pd_rd_i=0321965515&psc=1) on usability is called "Don't Make Me Think".
		* Consistency in design elements reduces surprise.
			* Example: a gear icon usually means "settings"
	* ... they improve development speed
		* Less back-and-forth between designers and product managers
		* Less back-and-forth between designers and programmers
		* Avoiding rebuilding similar components over and over in many slightly different ways
		* Less re-work for programmers due to arbitrary design decisions
			* It's more stable to build upon fundamental design principles.
* Because of these benefits, many apps that are built by modern dev teams use design systems.

### "Material Design": a practical example of a design system
* `Material Design` is an excellent design system from Google.
    * It's called "material" because it is inspired by physical materials -- textures, shadows, etc.
* Examples of Material Design [guidelines](https://material.io/design/guidelines-overview)
    * [Bottom Bars](https://material.io/components/app-bars-bottom)
	* [Floating Action Button](https://material.io/components/buttons-floating-action-button)
	* [Top Bar](https://material.io/components/app-bars-top)
* Material Design is very commonly used in Flutter applications and is also used in some web applications.
* Note: Material Design is just one design system. There are many design systems in the world, often custom-made by designers for a single app.

### The code that implements a design system
* Design systems are created by UX designers, not programmers.
* Design systems are not code. They are expressed using design artifacts like icons, typefaces, wireframes etc.
* But to actually apply a design system to an app requires code, of course.
* For Material Design, Google has provided this code: an entire component library, ready to use in Flutter.

### Material Design widget catalog
* Intro to the [widget catalog](https://docs.flutter.dev/development/ui/widgets)
* How to search for widgets in the catalog

### Pre-built vs custom-built widgets

#### Pre-built widgets
* Commonly used, thus battle-tested and predictable.
* Ready to use -- fast and easy.
* All common Material widgets are implemented by the official Flutter team, therefore:
	* Guaranteed well-written.
	* Also well-supported by the community.
		* You can report bugs.
		* You can check if developers worldwide already ran into issues
			* [example of issue](https://github.com/flutter/flutter/issues/106717)

#### Custom-built widgets
* Pre-built widgets have the benefits above, but...
* sometimes developers choose to create their own widget, because they:
	* don't know about existing Material solutions
	* need fewer features
	* feel more confident with custom implementation

* Careful programmers often consider which approach would be better to consider:
	* Is it safer to use a proven solution?
	* Will the effort of customizing an existing widget be greater than creating your own?

### Formative task
_proposed format: MCQ_

* raise the awareness of the popularity of Material design on the example of popular applications and their styles
* indicating how to search for widgets

### Summative task
_proposed format: code repo_

* encourage the use of sample widgets from Material design
* customizing the appearance of the widget
* enforcing the decision to choose your own implementation vs. using an existing solution
