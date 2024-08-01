// src/components/AdminDashboard.js
import React, { useEffect, useState } from "react";
import axios from "axios";

const AdminDashboard = () => {
  const [data, setData] = useState({
    students: [],
    parents: [],
    placements: [],
    events: [],
    feedbacks: [],
  });

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    const studentsResponse = await axios.get("/api/students");
    const parentsResponse = await axios.get("/api/parents");
    const placementsResponse = await axios.get("/api/placements");
    const eventsResponse = await axios.get("/api/events");
    const feedbacksResponse = await axios.get("/api/feedbacks");

    setData({
      students: studentsResponse.data,
      parents: parentsResponse.data,
      placements: placementsResponse.data,
      events: eventsResponse.data,
      feedbacks: feedbacksResponse.data,
    });
  };

  return (
    <div>
      <h1>Admin Dashboard</h1>
      <div>
        <h2>Students</h2>
        <ul>
          {data.students.map((student) => (
            <li key={student.id}>
              {student.name} - {student.department}
            </li>
          ))}
        </ul>
      </div>
      <div>
        <h2>Parents</h2>
        <ul>
          {data.parents.map((parent) => (
            <li key={parent.id}>
              {parent.name} - {parent.email}
            </li>
          ))}
        </ul>
      </div>
      <div>
        <h2>Placements</h2>
        <ul>
          {data.placements.map((placement) => (
            <li key={placement.id}>
              {placement.company} - {placement.position}
            </li>
          ))}
        </ul>
      </div>
      <div>
        <h2>Events</h2>
        <ul>
          {data.events.map((event) => (
            <li key={event.id}>
              {event.name} - {event.date}
            </li>
          ))}
        </ul>
      </div>
      <div>
        <h2>Feedbacks</h2>
        <ul>
          {data.feedbacks.map((feedback) => (
            <li key={feedback.id}>
              {feedback.content} - {feedback.rating}/5
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
};

export default AdminDashboard;
