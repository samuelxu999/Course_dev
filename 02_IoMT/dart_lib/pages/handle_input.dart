//reference:
// https://docs.flutter.dev/cookbook/forms/retrieve-input
// https://docs.flutter.dev/get-started/fundamentals/user-input

import 'package:flutter/material.dart';

// This is a demo page to show layout widgets
class DemoInputWidgets extends StatefulWidget {
  const DemoInputWidgets({super.key});

  @override
  State<DemoInputWidgets> createState() => _DemoInputUpdateState();
}

// This function update page given state change
class _DemoInputUpdateState extends State<DemoInputWidgets> {
  // Create a text controller and use it to retrieve the current value of the TextField.
  final textController = TextEditingController();

  @override
  void dispose() {
    // Clean up the controller when the widget is disposed.
    textController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Input Demo'),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16),
        child: TextField(
          controller: textController,
        ),
      ),
      floatingActionButton: FloatingActionButton(
        // When the user presses the button, show an alert dialog containing
        // the text that the user has entered into the text field.
        onPressed: () {
          showDialog(
            context: context,
            builder: (context) {
              return AlertDialog(
                // Retrieve the text the that user has entered by using the
                // TextEditingController.
                content: Text(textController.text),
              );
            },
          );
        },
        tooltip: 'Show me the value!',
        child: const Icon(Icons.text_fields),
      ),
    );
  }
}