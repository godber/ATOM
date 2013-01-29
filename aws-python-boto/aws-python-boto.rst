~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Amazon Web Services with Python and Boto
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Austin Godber | @godber | godber@uberhip.com


===============================================================================
Overview of AWS
===============================================================================

`Amazon Web Services <http://aws.amazon.com/>`_ includes the following services:

* **EC2** - Elastic Compute Cloud, Dynamically launch and manage virtual
  machines, EBS, Cloud Watch

* **S3** - Simple Storage Service, Store and retrieve files over HTTP

* **SNS** - Simple Notification Service, Send email or webhook based notifications

* **SQS** - Simple Queue Service, Send messages through a global queue, Cloud
  Front

* **RDS** - Relational Database Service, Managed MySQL Service


===============================================================================
Other AWS Services
===============================================================================

There are quite a few other AWS Services that won't be covered here:

* Elastic MapReduce

* SimpleDB

* Elastic Beanstalk

* CloudFormation

* Simple Email Service

* Route 53

* Virtual Private Cloud

* Elastic Load Balancing

* Flexible Payment Services


===============================================================================
Other AWS Utilities
===============================================================================

There are non programatic ways of interacting with AWS.

* http://console.aws.amazon.com/

* Firefox Plugins

  * ElasticFox

  * S3 Organizer

* s3sync

* Amazon provides command line tools as well but they are spread all over the
  place, a nuisance to setup, and rev too often to be convenient.

===============================================================================
Overview of Boto
===============================================================================

Boto is the python library that interacts with these services.  It is kept well
in sync with new services, which is very impressive.

* Docs: http://boto.cloudhackers.com/

* Project: http://code.google.com/p/boto/

* Github: https://github.com/boto/boto

===============================================================================
Understanding EC2
===============================================================================

* Availability Zones are "isolated" data centers within regions.

* **AMI** - Amazon Machine Image; pre Existing or make your own

* **Instance** - An instance of a running AMI and the resources allocated to it.

* **Pricing** - Pay as you go, by resource consumption

  * Compute Time - On demand, Spot, Reserved Pricing

  * Bandwidth - In and Out

  * Extras - EBS (Disk), Elastic IP, Cloud Watch, Load Balancing

* Security Groups - Firewall Rules

* NAT - Public Address and Private Address, Elastic IP

* Not optimized for single stack applications but for custom distributed
  systems.

===============================================================================
Launching an AMI with Boto
===============================================================================

See ec2-example1.py

Advanced Features:

* User Data - `Ubuntu CloudInit <https://help.ubuntu.com/community/CloudInit>`_

* EBS Volumes

* Elastic IPs

===============================================================================
Understanding S3
===============================================================================

The AWS Simple Storage Service is a basic data store that can be written to over
HTTP and read via HTTP or BitTorrent.

* Buckets, keys and metadata.

* Access Control - By AWS user or though signed URLs.

* Versioning

* Reduced redundancy

* AWS Import/Export - Sneakernet

* DNS CNAME, Index and Error Documenent mapping, good for static sites (blogophile)

* CloudFront - Content Distribution Network

===============================================================================
Uploading Files to S3
===============================================================================

For example, see the build function in the fabfile for this presentation:

.. sourcecode:: python

    import boto
    c = boto.connect_s3()
    b = c.get_bucket('presentations.uberhip.com')
    k = boto.s3.Key(b)
    k.key = "aws-python-boto/index.html"
    k.set_contents_from_filename(
      "aws-python-boto/index.html"
      )
    k.set_acl('public-read')
    k.set_metadata('Content-Type','text/html')

===============================================================================
Understanding SQS
===============================================================================

SQS is a reliable hosted queueing solution.

* Messages can remain in queue for 14 days.

* Messages are set to be invisible upon read as a locking mechanism.  These
  locks expire.

* Queues can be shared with various access control.

* See sqs-example1.py


===============================================================================
Understanding SNS
===============================================================================

The Simple Notification Service is a robust, hosted notification service.
Notifications can be in the form of email, HTTP(S) webhooks, or SQS.

* Topics

* Policy Management

  * Subscribers

  * Publishers

* Manage on web or with boto


===============================================================================
SNS Publish Example with Boto
===============================================================================

Notice there is no access control or authentication.

.. sourcecode:: python

  # Publish a message to a topic
  import boto
  c = boto.connect_sns()
  c.publish(
    # The Topic's ARN
    'arn:aws:sns:us-east-1:104167845052:test_topic',
    # The message
    'test publish'
  )

===============================================================================
Understanding RDS
===============================================================================

The Relational Database Service provides a hosted MySQL service and offers
advanced features.

* Use boto to

  * Create/Delete DBs

  * Replicate DBs

  * Create/Delete/Restore Snapshots

* These are AMIs too, so they have instance types and storage size.

* Think of it as an API to a MySQL host and MySQL admin.  At the DB level, its
  interacted with via a mysql client library or shell.

===============================================================================
Thanks
===============================================================================

* Thanks to the authors and documentors of the Boto library, from which I have derived my examples:

  * http://boto.cloudhackers.com/

* Thanks Morgan for his post on code snippets and S5.

  * http://morgangoose.com/blog/2010/09/12/using-rst-for-presentations/

* This work is licensed under the Attribution 3.0 Unported (CC BY 3.0) license:

  * http://creativecommons.org/licenses/by/3.0/

* Available online 
  
  * Source: https://github.com/godber/presentations/

  * Viewable: http://presentations.uberhip.com/aws-python-boto/

.. footer::
  Copyright Austin Godber, 2011
