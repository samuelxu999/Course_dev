// Importing necessary libraries and packages
import 'dart:convert';
import 'package:http/http.dart' as http;

// Call fitbit auth2.0 request to generate access token
Future<String> fitbitAuth(String authCode) async {
  final url=Uri.parse('[replace with your aws API gateway endpoint]');
  final response = await http.post(url,
    headers: <String, String>{
      'Content-Type': 'application/json; charset=UTF-8'
    },
    body: jsonEncode(<String,String>{ 
      "authorization_code": authCode
    })
  );
  // print(response.statusCode);
  // print(response.body);

  return response.body;
}

// Call fitbit refresh access token
Future<String> fitbitRefreshToken() async {
  final url=Uri.parse('[replace with your aws API gateway endpoint]');
  final response = await http.get(url,
    headers: <String, String>{
      'Content-Type': 'application/json; charset=UTF-8'
    }
  );
  // print(response.statusCode);
  // print(response.body);

  return response.body;
}