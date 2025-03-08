import 'package:flutter/material.dart';
import 'api_functions.dart';

// This is a demo page to show how to use http call API gateway to fetch Fitbit data and display on UI.
class QueryData extends StatefulWidget {
  const QueryData({super.key});

  @override
  State<QueryData> createState() => _QueryDataPageState();
}

// This function update page given state change
class _QueryDataPageState extends State<QueryData> {
  // define a Future object to handle results from a asyn function
  Future<String>? futureHeartRate;

  // define controller objects to handle user input datetime from UI text field widgets
  final TextEditingController _controller_startTime = TextEditingController();
  final TextEditingController _controller_endTime = TextEditingController();

  // All initial state and operations should be here
  @override
  void initState() {
    super.initState();
    // We set default datetime to simplify test.
    _controller_startTime.text='2025-02-14';
    _controller_endTime.text='2025-02-14';
  }

  @override
  void dispose() {
    // Clean up the controller when the widget is disposed.
    _controller_startTime.dispose();
    _controller_endTime.dispose();
    super.dispose();
  }

  // This function will be executed as press button.
  void _updateText() {

    // Call async function to retrive data from aws API gateway
    futureHeartRate = getHeartRate(_controller_startTime.text,_controller_endTime.text);

    // refresh page to show search results.
    setState(() {
      build(context);
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      // appBar: AppBar(
      //   title: const Text('Search Heart Rate'),
      // ),
      body: SingleChildScrollView(
        child: Column(
          children: <Widget>[
            Padding( 
              padding: const EdgeInsets.only(top: 110.0), 
            ),
            // Text Field: Input start date time
            Padding( 
              //padding: const EdgeInsets.only(left:15.0,right: 15.0,top:0,bottom: 0), 
              padding: EdgeInsets.symmetric(horizontal: 15), 
              child: TextField(
                controller: _controller_startTime,
                decoration: InputDecoration( 
                    border: OutlineInputBorder(), 
                    labelText: 'Start date time', 
                    hintText: 'Enter datatime: yyyy-mm-dd'), 
              ), 
            ),
            // Text Field: Input end date time
            Padding( 
              padding: const EdgeInsets.only( 
                  left: 15.0, right: 15.0, top: 15, bottom: 0), 
              //padding: EdgeInsets.symmetric(horizontal: 15), 
              child: TextField(   
                controller: _controller_endTime, 
                decoration: InputDecoration( 
                    border: OutlineInputBorder(), 
                    labelText: 'End date time', 
                    hintText: 'Enter datatime: yyyy-mm-dd'), 
              ), 
            ), 
          
            // Button: Data search button
            SizedBox( 
              height: 65, 
              width: 360, 
                child: Padding( 
                  padding: const EdgeInsets.only(top: 20.0), 
                  child: ElevatedButton( 
                    child: Text( 'Query Heart Rate', style: TextStyle(color: const Color.fromARGB(255, 3, 59, 105), fontSize: 20), 
                    ), 
                    // handle function after pressing button
                    onPressed: (){ 
                      // implement data access functions here
                      _updateText();
                    }, 

                  ), 
                ), 
            ),
            // Container: show data on screen given search results
            Container(
              margin: EdgeInsets.all(20),
              padding: EdgeInsets.all(20),
              child: buildFutureBuilder(),
            ),
          ],
        ),
      ),

    );
  }

  // This function will build widget to show fetched data on screen
  // FutureBuilder widget is used to perform asynchronous operations and rebuild the UI when the operation is complete
  FutureBuilder<String> buildFutureBuilder() {
    return FutureBuilder<String>(
      // listening Future object update
      future: futureHeartRate,
      // build UI given value of snapshot object
      builder: (context, snapshot) {
        if (snapshot.hasData) {
          // Display the fetched data when data is available
          return Center(child: Text(snapshot.data!));
        } else if (snapshot.hasError) {
          // Display an error message if there's an error
          return Text('${snapshot.error}');
        } else {
          if(futureHeartRate==null){
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