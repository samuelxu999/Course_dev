import 'package:flutter/material.dart';
import 'fitbit_auth.dart';
// import 'package:demo_code/pages/Stress.dart';

// This is home page after login
class HomePage extends StatefulWidget {
  const HomePage({super.key});

  @override
  State<HomePage> createState() => _HomePageState();
}

// This function update login page given state change
class _HomePageState extends State<HomePage> {

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      // appBar: AppBar(
      //   title: const Text('Home Page'),
      //   backgroundColor: Colors.blue,
      // ),
      body: SingleChildScrollView(
        child: Column(
          children: <Widget>[
            Padding( 
              padding: const EdgeInsets.only(top: 50.0), 
            ),
            Padding( 
              //padding: const EdgeInsets.only(left:15.0,right: 15.0,top:0,bottom: 0), 
              padding: EdgeInsets.symmetric(horizontal: 15), 
            ), 
            // Input user name
            Padding( 
              //padding: const EdgeInsets.only(left:15.0,right: 15.0,top:0,bottom: 0), 
              padding: EdgeInsets.symmetric(horizontal: 15), 
              child: Text( 
                'Welcome to home page'
              ), 
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
                        child: Text( 'Log out', style: TextStyle(color: const Color.fromARGB(255, 3, 59, 105), fontSize: 20), 
                        ), 
                        // handle function here
                        onPressed: (){ 
                          // Navigate to login page when tapped.
                          Navigator.pop(context);
                        },       
                      ), 
                    ), 

              ),
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
                        child: Text( 'Fitbit Authorization', style: TextStyle(color: const Color.fromARGB(255, 3, 59, 105), fontSize: 20), 
                        ), 
                        // handle function here
                        onPressed: (){ 
                          // Navigate to fitbit token setup page when tapped.
                          Navigator.push(context,MaterialPageRoute(builder: (context) => FitbitAuth()));
                          
                        },       
                      ), 
                    ), 

              ),
            ), 
          ]

        ),

      ),
    );
  }
}