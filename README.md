This is a Message Processing application to process the input messages as per requirement.

Below are different modules:

1.) Message Generator: To prepare the messages as per below given requirement.

	Message Type 1 – contains the details of 1 sale
	
	Message Type 2 – contains the details of a sale and the number of occurrences of that sale.
	
	Message Type 3 – contains the details of a sale and an adjustment operation to be applied to all stored sales of this product type. Operations can be add, subtract, or multiply  e.g Add 20p apples would instruct your application to add 20p to each sale of apples you have recorded.

2.) Message Processor: To process the messages as per given requirement.

	All sales must be recorded.
	
	All messages must be processed.
	
	After every 10th message received your application should log a report detailing the number of sales of each product and their total value.
	
	After 50 messages your application should log that it is pausing, stop accepting new messages and log a report of the adjustments that have been made to each sale type while the application was running.

3.) Single Sale Processor: To handle messge type 1

4.) Multiple Sale Processor: To handle messge type 2

5.) Adjustment Sale Processor: To handle message type 3

6.) Unprocessed Recorder: To record unprocessed messages with reason

Below are utility files to support modules:

1.) Constants: Keep string constants centralized.

2.) common: Keep the globally used variables.

3.) config reader: to read data from json config file

Below is test module:

1.) Test Message Generator: Create controlled test data to test the system.


To run the system, run the Message Generator module.

To test the system with controlled data, run the Test Message Generator module.

python version used: 3.6.3
