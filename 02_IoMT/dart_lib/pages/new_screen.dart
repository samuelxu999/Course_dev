import 'package:flutter/material.dart';

// This is a demo page to show stree score input page
class NewPage extends StatefulWidget {
  const NewPage({super.key});

  @override
  State<NewPage> createState() => _NewPageState();
}

// This function update page given state change
class _NewPageState extends State<NewPage> {
  // Default placeholder text.
  String textToShow = 'This is a new screen.';

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      // 1) You can use back button on app bar to return previous screen.
      appBar: AppBar(
        title: const Text('New Screen'),
      ),
      body: SingleChildScrollView(
        child: Column(
          children: <Widget>[
            Padding( 
              padding: const EdgeInsets.only(top: 50.0), 
              child: Text(textToShow),
            ),
            Padding( 
              padding: const EdgeInsets.only( 
                left: 15.0, right: 15.0, top: 15, bottom: 0), 
                child: SizedBox( 
                  height: 65, 
                  width: 360, 
                    child: Padding( 
                      padding: const EdgeInsets.only(top: 20.0), 
                      child: ElevatedButton( 
                        child: Text( 'Back to main screen', style: TextStyle(color: const Color.fromARGB(255, 3, 59, 105), fontSize: 20), 
                        ), 
                        // handle function here
                        onPressed: (){ 
                          // 1) You can use Navigator.pop() in a button's callback function to return previous screen.
                          // Navigate to main screen when tapped.
                          Navigator.pop(context);
                        },       
                      ), 
                    ), 

              ),
            ), 
          ],
        ),
      ),

    );
  }
}