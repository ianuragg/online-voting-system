<h1>Online Voting System</h1>
This is a web application that allows users to create and participate in online elections. It is built using Django, a Python web framework.

<h2>Features</h2>
<ul>
<li>User Registration / Login: Users can register and log in to the system using their email and password.</li>
<li>Custom Candidate Registration - (Admin): Admin users can add candidates for different positions in an election. They need to provide the candidate’s name, bio, photo and position.</li>
<li>Custom Election Registration - (Admin): Admin users can create new elections and set their title, start date, and end date.</li>
<li>Active / Expired Elections: Users can view the list of active and expired elections. They can also see the number of votes cast for each election.</li>
<li>Election Details: Users can click on an election title to see more details about it, such as the candidates, positions, start date, end date and status (ongoing or closed).</li>
<li>Candidate Page: Users can click on a candidate’s name to see their bio and photo.</li>
<li>Voting Process: Users can vote for their preferred candidates in an active election. They can also preview their ballot before submitting it.</li>
<li>Vote Confirmation: Users can see a confirmation message after submitting their vote.</li>
<li>Result Page: Users can see the results of an expired election by clicking on its title. They can see the total number of votes cast for each candidate and position.</li>
</ul>

<h2>Installation</h2>
<p>To run this project locally, you need to have Python 3.x and Django 3.x installed on your machine.</p>

You also need to install some dependencies using pip:
<pre>pip install -r requirements.txt</pre>

Then you need to create a database using SQLite:
<pre>python manage.py migrate</pre>

You can create an admin user using this command:
<pre>python manage.py createsuperuser</pre>

You can run the server using this command:
<pre>python manage.py runserver</pre>

You can access the web application at http://localhost:8000/
