// ignore_for_file: non_constant_identifier_names

import 'package:flutter/material.dart';
import 'dart:async';
import 'package:fitbit_auth_demo/pages/api_functions.dart';

// This is a page to complete fitbit authorizzation and get access_token
class FitbitAuth extends StatefulWidget {
  const FitbitAuth({super.key});

  @override
  State<FitbitAuth> createState() => _FitbitAuthState();
}

// This function update page given state change
class _FitbitAuthState extends State<FitbitAuth> {

  StreamController<String> controller = StreamController<String>();
  late StreamSubscription<String> myStreamSubscription;

  final TextEditingController _controller_authcode = TextEditingController();
  Future<String>? futureData;

// This function will be executed as press button.
void _updateText(int opCode) {
  // Call async function to retrive data from aws API gateway
  // print(_controller_authcode.text);
  if(opCode==0){
    futureData = fitbitAuth(_controller_authcode.text);
  }
  else{
    futureData = fitbitRefreshToken();
  }

  // refresh page to show search results.
  setState(() {
    build(context);
  });
}

@override
  Widget build(BuildContext context) {
    return Scaffold(
      // 1) You can use back button on app bar to return previous screen.
      appBar: AppBar(
        title: const Text('Fitbit Authorization'),
      ),
      body: SingleChildScrollView(
        child: Column(
          children: <Widget>[
            // --------------- Input access code text field ----------------------
            Padding( 
              padding: const EdgeInsets.only( 
                  left: 15.0, right: 15.0, top: 15, bottom: 0), 
              //padding: EdgeInsets.symmetric(horizontal: 15), 
              child: TextField(   
                controller: _controller_authcode, 
                decoration: InputDecoration( 
                    border: OutlineInputBorder(), 
                    labelText: 'Input fitbit authorization code', 
                    hintText: 'auth code from redirect url'), 
              ), 
            ),
            // ----------------- Request access token button ----------------
            Padding( 
              padding: const EdgeInsets.only( 
              left: 15.0, right: 15.0, top: 15, bottom: 0), 
              child: SizedBox( 
                height: 65, 
                width: 360, 
                child: Padding( 
                  padding: const EdgeInsets.only(top: 20.0), 
                  child: ElevatedButton( 
                    child: Text( 'Request Access Token', style: TextStyle(color: const Color.fromARGB(255, 3, 59, 105), fontSize: 20), 
                    ), 
                    // handle function here
                    onPressed: (){ 
                      _updateText(0);
                    },       
                  ), 
                ), 
              ),
            ),
            // -------------- Refresh access token button -------------
            Padding( 
              padding: const EdgeInsets.only( 
              left: 15.0, right: 15.0, top: 15, bottom: 0), 
              child: SizedBox( 
                height: 65, 
                width: 360, 
                child: Padding( 
                  padding: const EdgeInsets.only(top: 20.0), 
                  child: ElevatedButton( 
                    child: Text( 'Refresh Access Token', style: TextStyle(color: const Color.fromARGB(255, 3, 59, 105), fontSize: 20), 
                    ), 
                    // handle function here
                    onPressed: (){ 
                      _updateText(1);
                    },       
                  ), 
                ), 
              ),
            ),
            Container(
              margin: EdgeInsets.all(20),
              padding: EdgeInsets.all(20),
              // ---------------- This is future build based on response of token authorization ---------------
              child: buildFutureBuilder(),
            ),
          ],
        ),
      ),
    );
  }

  FutureBuilder<String> buildFutureBuilder() {
    return FutureBuilder<String>(
      future: futureData,
      builder: (context, snapshot) {
        if (snapshot.hasData) {
          // Display the response when data is available
          return Center(child: Text(snapshot.data!));
        } else if (snapshot.hasError) {
          // Display an error message if there's an error
          return Text('${snapshot.error}');
        } else {
          if(futureData==null){
            // Display a default message as initial state
            return Text('No Data.');
          }
          else{
            // Display a loading indicator while waiting for data
            return Center(child: CircularProgressIndicator());
          }
        }
      },
    );
  }
}
