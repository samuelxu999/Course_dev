import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'api_functions.dart';

// This is a demo page to show stree score input page
class ApiTest extends StatefulWidget {
  const ApiTest({super.key});

  @override
  State<ApiTest> createState() => _ApiTestPageState();
}

// This function update page given state change
class _ApiTestPageState extends State<ApiTest> {
  // Default placeholder text.
  String textToShow = 'Show you data here';

  void _updateText() {

    setState(() {

      build(context);
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('API Test'), // Set the app bar title
      ),
      body: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Container(
            margin: EdgeInsets.all(20),
            padding: EdgeInsets.all(20),
            child: FutureBuilder<String>(
              future: getSteps('2025-02-10','2025-02-12'),
              // future: getHW(),
              builder: (context, snapshot) {
                if (snapshot.hasData) {
                  // Display the fetched data when data is available
                  return Center(child: Text(snapshot.data!));
                } else if (snapshot.hasError) {
                  // Display an error message if there's an error
                  return Text('${snapshot.error}');
                } else {
                  // Display a loading indicator while waiting for data
                  return Center(child: CircularProgressIndicator());
                }
              },
            ),
          ),
          // Button to fetch a new joke
          ElevatedButton(onPressed: _updateText, child: Text("Update Data")) 
        ],
      ),
    );
  }
}