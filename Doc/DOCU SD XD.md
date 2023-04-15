![](Aspose.Words.5127c885-7ffd-4f29-b5f1-44707b9a5d7d.001.png)
# Table of content
* [1. A brief introduction to the system’s features and goals.](#1-a-brief-introduction-to-the-systems-features-and-goals)


* [2. System implementation, including design choices.](#2-system-implementation-including-design-choices-)


* [3. A discussion on your final version of the system justifying to which extent the goals have been fulfilled.](#a-nametoc132472919a3-a-discussion-on-your-final-version-of-the-system-justifying-to-which-extent-the-goals-have-been-fulfilled-)


* [4. Coherent and concise answers to the previously proposed questions](#a-nametoc132472919a3-a-discussion-on-your-final-version-of-the-system-justifying-to-which-extent-the-goals-have-been-fulfilled-)

    * [1. All communication steps of the system based on the four types of communication (synchronous/asynchronous, pull/push, transient/persistent, stateless/stateful). Also include their pattern and cardinality (one-to-one, one-to-all...).](#1-all-communication-steps-of-the-system-based-on-the-four-types-of-communication-synchronousasynchronous-pullpush-transientpersistent-statelessstateful-also-include-their-pattern-and-cardinality-one-to-one-one-to-all)
    * [2. Mention which communication type is more appropriate for each step and justify your decision in terms of scalability and fault tolerance.](#1-all-communication-steps-of-the-system-based-on-the-four-types-of-communication-synchronousasynchronous-pullpush-transientpersistent-statelessstateful-also-include-their-pattern-and-cardinality-one-to-one-one-to-all)
    * [3. Are there single points of failure in the system? How could you resolve them?](#a-nametoc132472922a3-are-there-single-points-of-failure-in-the-system-how-could-you-resolve-them-)
    * [4. Regarding system decoupling, what does a Message Oriented Middleware (MOM) such as RabbitMQ provide?	7](#a-nametoc132472923a4-regarding-system-decoupling-what-does-a-message-oriented-middleware-mom-such-as-rabbitmq-provide-)


[5. Briefly describe Redis’ utility as a storage system in this architecture.](#a-nametoc976184515aa-nametoc132472924a5-briefly-describe-redis-utility-as-a-storage-system-in-this-architecture)


## 1. A brief introduction to the system’s features and goals.

Our main goal in this task was to build from scratch two models of communications. Firstly, one using direct communication and the other using an indirect one. 

On the one hand, we’ve built a load balancer using a round-robin fashion. The servers are opened with the script that we’ve built and the other is the one responsible for delivering the messages from sensor to server and to terminal.  

On the other hand, on the indirect communication we’ve used RabbitMQ as a proxy to communicate the sensor, server, and terminal.

A more detailed analysis of both approaches will be done across the documentation.

## 2. System implementation, including design choices. 

When it comes to the decisions, we’ve chosen to design this system, we can highlight the following:

Regarding to the direct communication, we’ve used Redis in a remote server. This way, both of us were able to access the same data and in case we had a problem with our system, data wouldn’t be lost. We would have wanted to implement a frontend to visualize data in a more sophisticated way but we hadn’t got time to it.

When it comes to the second part, we’ve also made use of the server-located Redis and also RabbitMQ is stored in this server. In the README.md file, we show the user and password in case you would want to access the RabbitMQ interface to check the message queues.

Last of all, data visualization has been made with matplotlib and we recommend to use PyCharm or any Jetbrains IDE to visualize data with the SciView. 

![](Aspose.Words.5127c885-7ffd-4f29-b5f1-44707b9a5d7d.002.png)

Terminal’s ports have been hardcoded in the first part and we use ports ‘5002, 5003 and 5004’ for the servers.

We started off the task with the XML-RPC approach but then we saw some things, that made us change our mind: gRPC is a modern, high-performance framework for remote procedure calls (RPC) that uses the Protocol Buffers binary serialization format, while XML-RPC is an older, simpler RPC protocol that uses XML as its data format. Here are some reasons why gRPC is considered better than XML-RPC:

In our opinion, gRPC is a better choice than XML-RPC for building distributed systems due to its faster performance, better interoperability across languages and platforms, support for bidirectional streaming, type safety, and extensibility. We believe that gRPC's use of binary serialization, which is more compact and faster, along with its support for pluggable authentication, load balancing, and service discovery mechanisms make it a more modern and efficient way of building distributed systems compared to XML-RPC.

In contrast, XML-RPC is limited to HTTP and XML-based communication, supports only single-request and single-response messages, and has limited support for authentication, load balancing, and service discovery. However, we acknowledge that the choice of RPC framework ultimately depends on specific project requirements and constraints.

Seeing all this key points , gRPC provides a more modern, efficient, and flexible way of building distributed systems compared to XML-RPC. However, it may not be the best choice for all scenarios, and the choice of RPC framework will depend on specific project requirements and constraints.


## <a name="_toc132472919"></a>3. A discussion on your final version of the system justifying to which extent the goals have been fulfilled. 

We would have liked to make the ports more dynamic, so that they aren’t harcoded in the code.

Despite the main goals have been fulfilled, we would like the task to me more all arround full stack to learn more technologies and the most important to deliver a better output to the user, because the python plots are kind of a poor resource. If we had more time we would have liked to create a REST API and send data to a frontend.

## <a name="_toc132472920"></a>4. Coherent and concise answers to the previously proposed questions


### 1. All communication steps of the system based on the four types of communication (synchronous/asynchronous, pull/push, transient/persistent, stateless/stateful). Also include their pattern and cardinality (one-to-one, one-to-all...).

In our system there have been multiple communication steps from different types.


1. Firstly we can start off with the first part the communication with the sensor, independently of the type of each pollution or meteo data. The data is being sent to the load balancer so we are using synchronous communication, because the sender and the receiver must be active at the same time, the communication is initiated by the sender. And the receiver waits for the message to arrive, the communication patterns in synchronous communication are request response. The communication is statless and non persistent beacuse it is not stored. It has a N sensor to 1 LB relation:

![](Aspose.Words.5127c885-7ffd-4f29-b5f1-44707b9a5d7d.003.png)



1. Then the load balancer chooses one server to process the data. We  have to point out that in the first implementation (direct) this is done in the following way we use gRPC on the first part of the communication so the client is the sensor and the server is the load balancer and then the client becomes load balancer and the data is sent to the server in this case the server. In all gRPC comunications are made in push mechanisms. The client sends data to the server, and the server processes the data and sends a response back to the client. 



1. Thirdly the other part of communication of this process is between the load balancer and the server so the load balancer processes the data and sends it to a server with a round Robin fashion. Then there are no servers waiting for the info to be sent so this one is asynchronous communication. In asynchronous communication the sender and the receiver do not need to be active at the same time. The communication is initiated by the sender in this case the load balancer, and the receiver, the server will receive the message when it’s available. The communication patterns in asynchronous communication are message queue & call back (used in RabbitMQ). 

![](Aspose.Words.5127c885-7ffd-4f29-b5f1-44707b9a5d7d.004.png)





1. After the data is recieved, the server calculates the Wellness and is stored to the Redis database. Here we can say that it’s the only part from the system (despite the terminal and the graphic visualization) that data is being stored so the communication process is stateful. In the all other previous processes the communication is stateless.


1. Then the proxy gets the data from the database during the time of the tumbling window and the methods of the terminalService get the calculated average and standard deviaton. The data is stored in a terminal array (stateful and persistent). Finally the data gets ploted. This latest is a push communication because the server is sending data to the client without the client explicitly requesting it. Specifically, the **SendWellnessResults** function in the **TerminalServiceServicer** class is called by the client to send wellness results. Finally This is a synchronous (blocking) gRPC server implementation. ![](Aspose.Words.5127c885-7ffd-4f29-b5f1-44707b9a5d7d.005.png)

To develop the second part, which corresponds to the indirect model, we’ve made use of the different technologies that were mentioned. 

We now lose the load balancer and make use of RabbitMQ, which provides us a messaging queue where we can drop our messages and win message decoupling.

To design the sensor-server communication, we’ve chosen the working queues, in which we can save messages in a queue and distribute them among several workers. When it comes to the proxy-terminal communication, we’ve used the publish/subscribe instead, which we use to send the same data to several terminals at once. We do so by creating a queue at the proxy and getting subscribed at the terminal, so when a message is pushed, we’ll be notified and we’ll be able to plot the results.

Both queues have its pros and conts and each of it is used on a different scenario.



### <a name="_toc132472921"></a>2. Mention which communication type is more appropriate for each step and justify your decision in terms of scalability and fault tolerance. 

To make a distributed system scalable and fault-tolerant, there are several strategies that can be implemented:

1\. **Partitioning**: is the process of breaking a large database or system into smaller, more manageable parts. Each one can be located on a different server or node, which increases scalability and fault tolerance by distributing the load and minimizing the impact of any one failure. In our case this system wasn’t necessary because de data sent was quite simple and fast to process. If we had a large dataset it could have been a nice option.

2\. **Replication**: involves making copies of data or services on multiple servers or nodes. This strategy ensures that if one server fails, there are still other copies of the data available, thus improving fault tolerance. We could have implemented replication on the terminal to store the results and have more persistent communication. We could have used Redis or other kind of database. 

3\. **Load Balancing**: Load balancing distributes the workload across multiple servers or nodes. This ensures that no single server is overloaded and improves scalability by allowing the system to handle more requests. We have used this system in our application, so that one node is never overloaded with too many requests. 

4\. **Redundancy**: Redundancy involves creating backup systems or nodes that can take over in case of a failure. This ensures that the system remains available even if one or more nodes fail. It coluld be implemented, but using round robin, if one server fails other would carry the extra load, so that the system wouldn’t stop.

On the other hand, RabbitMQ can handle lots of node so scaling up horizontally is not a problem. 


### <a name="_toc132472922"></a>3. Are there single points of failure in the system? How could you resolve them? 

Yes, there are potential single points of failure in the system. For example, if a sensor node fails, the entire system may become unavailable, as it would not be able to process new tasks or receive updates from the worker nodes.

To solve this issue, we have catched the exception that if the server is not working, catches another one from the harcoded list of ports. If no server is available, the load balancer notifies the user and the system stops working. Whenever the server is back again, if the load balancer sends a request to it, connection will be established again and it will continue working as if nothing happened.


### <a name="_toc132472923"></a>4. Regarding system decoupling, what does a Message Oriented Middleware (MOM) such as RabbitMQ provide? 

One of the key features of RabbitMQ is message queuing, which allows messages to be stored in a queue until they can be processed by a consumer. This decouples the producers from the consumers, enabling them to operate independently and without interference from each other.

Another important feature of RabbitMQ is its support for the publish/subscribe model, which is the one we’ve chose. Here, multiple consumers can subscribe to the same message queue. 

This way, producers, which are sensors and the proxy, cand send messages to the subscribers without even knowing who they are. The same happens the other way around, meaning that the consumers can consume messages without the need to know who has sent that message.

This feature allows us to scale horizontally, because RabbitMQ supports working with thousands of consumers and servers at once.

Finally, RabbitMQ provides reliable message delivery, including message persistence and automatic redelivery in case of failures. This ensures that messages are not lost and are delivered to the intended recipient even if the system experiences any failure or goes down. By using RabbitMQ as a middleware, we’ve been able to see the potential it has and we’ve managed to create a low-level system stored in a server, although fault tolerance still has not been implemented.

## <a name="_toc976184515"></a><a name="_toc132472924"></a>5. Briefly describe Redis’ utility as a storage system in this architecture.

Redis has been recommended as a possible solution for implementing a caching layer in this architecture due to its various advantages. Keeping frequently accessed data in memory paves way for faster retrieval times; thereby improving system performance and scalability remarkably. It also supports different data structures such as strings, hashes, lists and sets accommodating varied requirements of users. Moreover Redis offers reliable backup with its persistence feature rendering constant support even during failure periods or downtimes. By incorporating Redis, the architecture can be optimized to improve its performance, scalability, and fault tolerance which are critical traits for any system. Redis adds significant value by enhancing these features of the system.

At first we wanted to implement Redis’ publish/subscribe system, but we noticed that it’s not as scalable as RabbitMQ is & it doesn’t support messages’ ACK out of the box.

![](Aspose.Words.5127c885-7ffd-4f29-b5f1-44707b9a5d7d.006.png)















