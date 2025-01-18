// Referece:
// https://www.geeksforgeeks.org/what-is-widgets-in-flutter/
// https://docs.flutter.dev/get-started/flutter-for/android-devs
import 'package:flutter/material.dart';

// This is a demo page to show StatefulWidgets
class DemoStatefulWidgets extends StatefulWidget {
  const DemoStatefulWidgets({super.key});

  @override
  State<DemoStatefulWidgets> createState() => _AppPageUpdateState();
}

// This function update page given state change
class _AppPageUpdateState extends State<DemoStatefulWidgets> {
  // Default placeholder text.
  String textToShow = 'This a default message.';

  void _updateText() {
    setState(() {
      // Update the text.
      textToShow = 'Updated message: Hello World';
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Demo App'),
      ),
      body: Center(child: Text(textToShow)),
      floatingActionButton: FloatingActionButton(
        onPressed: _updateText,
        tooltip: 'Update Text',
        child: const Icon(Icons.update),
      ),
    );
  }
}

// This is a demo page to show StatelessWidgets.
class DemoStatelessWidgets extends StatefulWidget {
  const DemoStatelessWidgets({super.key});

  @override
  State<DemoStatelessWidgets> createState() => _StaticAppPageState();
}

// This function update page given state change
class _StaticAppPageState extends State<DemoStatelessWidgets> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      // Set the background color of the scaffold
      backgroundColor: Colors.lightGreen,
      appBar: AppBar(
        // Set the background color of the app bar
        backgroundColor: Colors.green,
        // Set the title of the app bar
        title: const Text("This is a static page"),
      ),
      // The main body of the scaffold
      body: const Center(
        // Display a centered text widget
        child: Text(
          "Hello World!!",
          // Apply text styling
          style: TextStyle(
            fontSize: 24,          // Set font size
            fontWeight: FontWeight.bold, // Set font weight
          ),
        ),
      ),
    );
  }
}
