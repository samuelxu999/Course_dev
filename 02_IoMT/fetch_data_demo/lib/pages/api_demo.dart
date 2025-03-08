// Importing necessary libraries and packages
import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

// This is a demo page to show stree score input page
class CallAPI extends StatefulWidget {
  const CallAPI({super.key});

  @override
  State<CallAPI> createState() => _CallAPIState();
}

class Joke {
  String id;
  String value;

  Joke.fromJson(Map<String, dynamic> json)
      : id = json['id'],
        value = json['value'];
}

class _CallAPIState extends State<CallAPI> {
  // Function to fetch a random Chuck Norris joke from an API
  Future<Joke> fetchJoke() async {
    final response =
        await http.get(Uri.parse("https://api.chucknorris.io/jokes/random"));

    if (response.statusCode == 200) {
      return Joke.fromJson(jsonDecode(response.body));
    } else {
      throw Exception('Failed to fetch joke');
    }
  }

  // Function to change and update the displayed joke
  void changeJoke() {
    setState(() {
      // Rebuild the widget to fetch and display a new joke
      build(context);
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Chuck Norris Jokes'), // Set the app bar title
      ),
      body: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Container(
            margin: EdgeInsets.all(20),
            padding: EdgeInsets.all(20),
            child: FutureBuilder<Joke>(
              future: fetchJoke(),
              builder: (context, snapshot) {
                if (snapshot.hasData) {
                  // Display the fetched joke when data is available
                  return Center(child: Text(snapshot.data!.value));
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
          ElevatedButton(onPressed: changeJoke, child: Text("Next Joke")) 
        ],
      ),
    );
  }
}