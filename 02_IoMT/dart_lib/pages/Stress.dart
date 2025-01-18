import 'package:flutter/material.dart';

// This is a demo page to show stree score input page
class StressPage extends StatefulWidget {
  const StressPage({super.key});

  @override
  State<StressPage> createState() => _StressPageState();
}

// This function update page given state change
class _StressPageState extends State<StressPage> {
  // Default placeholder text.
  String textToShow = 'You need input your stree score.';

  void _updateText() {
    setState(() {
      // Update the text.
      textToShow = 'I am feel good!';
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      // appBar: AppBar(
      //   title: const Text('Streefull Score Page'),
      //   leading: IconButton(onPressed: (){
      //     Navigator.pop(context);
      //   }, icon: Icon(Icons.arrow_back)),
      // ),
      body: Center(child: Text(textToShow)),
      floatingActionButton: FloatingActionButton(
        onPressed: _updateText,
        tooltip: 'Update Text',
        child: const Icon(Icons.update),
      ),
    );
  }
}