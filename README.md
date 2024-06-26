<h1>Hotel Recommendation System</h1> 

<br>

<strong>-->Problem Statement</strong>
<p>◼ A hotel recommendation system aims to predict which hotel a user is most likely to choose from among all hotels.</p>
<p>◼ Recommendation System is an information filtering technique, which provide users with information, which he/she may be interested in.</p>
<br>

<strong>-->DATASET</strong>
<p>Dataset from kaggle : https://www.kaggle.com/jiashenliu/515k-hotel-reviews-data-in-europe/download</p>
<p>◼ This dataset contains 515,738 hotel’s.</p>
<p>◼ The dataset contain countries of Europe such as United Kingdom, Netherland, Spain, Austria, Italy.</p>
<strong>Features of Dataset</strong>
<p>Hotel_Name, Hotel_Address, Average_Score, Countries, Tags</p>
<br>

<strong>-->Technique Used</strong>
<p>Applied <b>Cosine Similarity</b> to identify similar document in text analytics</p>
<br>

<strong>-->EXISTING SYSTEM</strong>
<p>◼ In the existing system there was no option for the purpose of visit.</p>
<p>◼ So we have developed a model where the user can state the purpose of visit and based on that the hotels are predicted</p>
<br>

<strong>-->PROPOSED SYSTEM</strong>
<p>◼ Creating a system to recommend a hotel based on client’s location and type of trip</p>
<p>◼ It recommends the best rated hotels based on the following criteria</p>
<p>1) Purpose of Visit</p>
<p>2) Countries</p>
<br>

<strong>-->SYSTEM OUTPUTS</strong>
<p>Country: Netherlands, Purpose of Trip: Leisure</p>
<table><tr>
<td> 
  <p align="center" style="padding: 10px">
    <img alt="Forwarding" src="/images/Output1.jpg" width="900">
    <br>
  </p> 
  
</td>
</tr></table>
<p>Country: Italy, Purpose of Trip: Business</p>
<table><tr>
<td> 
  <p align="center" style="padding: 10px">
    <img alt="Forwarding" src="/images/Output2.jpg" width="850">
    <br>
  </p>
</td>
</tr></table>
