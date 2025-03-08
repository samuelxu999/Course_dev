import 'package:flutter/material.dart';
import 'api_functions.dart';

// This is a demo page to show how to use http call API gateway to save Fitbit data.
class SaveData extends StatefulWidget {
  const SaveData({super.key});

  @override
  State<SaveData> createState() => _SaveDataPageState();
}

// This function update page given state change
class _SaveDataPageState extends State<SaveData> {
  Future<String>? futureHeartRate;
  final TextEditingController _controller_collectTime = TextEditingController();

  // All initial state and operations should be here
  @override
  void initState() {
    super.initState();
    // We set default datetime to simplify test.
    _controller_collectTime.text='2025-02-14';
  }

  @override
  void dispose() {
    // Clean up the controller when the widget is disposed.
    _controller_collectTime.dispose();
    super.dispose();
  }

  // This function will be executed as press button.
  void _updateText() {

    // Call async function to retrive data from aws API gateway
    futureHeartRate = saveHeartRate(_controller_collectTime.text);

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
            // Input start date time
            Padding( 
              //padding: const EdgeInsets.only(left:15.0,right: 15.0,top:0,bottom: 0), 
              padding: EdgeInsets.symmetric(horizontal: 15), 
              child: TextField(
                controller: _controller_collectTime,
                decoration: InputDecoration( 
                    border: OutlineInputBorder(), 
                    labelText: 'Collect date time', 
                    hintText: 'Enter datatime: yyyy-mm-dd'), 
              ), 
            ),          
            // Data search button
            SizedBox( 
              height: 65, 
              width: 360, 
                child: Padding( 
                  padding: const EdgeInsets.only(top: 20.0), 
                  child: ElevatedButton( 
                    child: Text( 'Save Heart Rate', style: TextStyle(color: const Color.fromARGB(255, 3, 59, 105), fontSize: 20), 
                    ), 
                    // handle function after pressing button
                    onPressed: (){ 
                      // implement data access functions here
                      _updateText();
                    }, 

                  ), 
                ), 
            ),
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

  // this function will build widget to show fetched data on screen
  FutureBuilder<String> buildFutureBuilder() {
    return FutureBuilder<String>(
      future: futureHeartRate,
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