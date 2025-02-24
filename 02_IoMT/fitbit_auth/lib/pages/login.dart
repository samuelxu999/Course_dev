import 'package:flutter/material.dart';
import 'package:fitbit_auth_demo/pages/navigate.dart';

// This is a demo page to show StatefulWidgets
class LoginPage extends StatefulWidget {
  const LoginPage({super.key});

  @override
  State<LoginPage> createState() => _LoginPageState();
}

// This function update login page given state change
class _LoginPageState extends State<LoginPage> {

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      // appBar: AppBar(
      //   title: const Text('Login Page'),
      // ),
      body: SingleChildScrollView(
        child: Column(
          children: <Widget>[
            Padding( 
              padding: const EdgeInsets.only(top: 110.0), 
            ),
            // Input user name
            Padding( 
              //padding: const EdgeInsets.only(left:15.0,right: 15.0,top:0,bottom: 0), 
              padding: EdgeInsets.symmetric(horizontal: 15), 
              child: TextField( 
                decoration: InputDecoration( 
                    border: OutlineInputBorder(), 
                    labelText: 'Phone number, email or username', 
                    hintText: 'Enter valid email id as abc@gmail.com'), 
              ), 
            ),
            // Input password
            Padding( 
              padding: const EdgeInsets.only( 
                  left: 15.0, right: 15.0, top: 15, bottom: 0), 
              //padding: EdgeInsets.symmetric(horizontal: 15), 
              child: TextField(   
                obscureText: true, 
                decoration: InputDecoration( 
                    border: OutlineInputBorder(), 
                    labelText: 'Password', 
                    hintText: 'Enter secure password'), 
              ), 
            ), 
          
            // Sign in button
            SizedBox( 
              height: 65, 
              width: 360, 
                child: Padding( 
                  padding: const EdgeInsets.only(top: 20.0), 
                  child: ElevatedButton( 
                    child: Text( 'Log in ', style: TextStyle(color: const Color.fromARGB(255, 3, 59, 105), fontSize: 20), 
                    ), 
                    // handle function here
                    onPressed: (){ 
                      // Authentication here before jump to home page

                      // Navigate to home page when tapped.
                      Navigator.push(context,MaterialPageRoute(builder: (context) => NavigatePage()));
                    }, 

                  ), 
                ), 
            ),

            //forget password
            SizedBox( 
              child: Center( 
                child: Row( 
                  children: [ 

                    Padding( 
                      padding: const EdgeInsets.only(left: 62), 
                      child: Text('Forgot your login details? '), 
                    ), 

                    Padding( 
                      padding: const EdgeInsets.only(left:1.0), 
                      child: InkWell( 
                        onTap: (){ 
                          print('hello'); 
                        }, 
                          child: Text('Get help logging in.', style: TextStyle(fontSize: 14, color: Colors.blue),)), 
                    ) 
                  ], 
                ), 
              ) 
            ) 

          ],
        ),
      ),

    );
  }
}