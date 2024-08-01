// src/App.js
import React from "react";
import StudentProfile from "./components/StudentProfile";
import ParentPortal from "./components/ParentPortal";
import PlacementHub from "./components/PlacementHub";
import OpportunityDirectory from "./components/OpportunityDirectory";
import EventManagement from "./components/EventManagement";
import FeedbackRatings from "./components/FeedbackRatings";
import AdminDashboard from "./components/AdminDashboard";

const App = () => {
  return (
    <div>
      <h1>Welcome to Student Hub</h1>
      <StudentProfile />
      <ParentPortal />
      <PlacementHub />
      <OpportunityDirectory />
      <EventManagement />
      <FeedbackRatings />
      <AdminDashboard />
    </div>
  );
};

export default App;
