// src/components/OpportunityDirectory.js
import React, { useState, useEffect } from "react";
import axios from "axios";

const OpportunityDirectory = () => {
  const [opportunities, setOpportunities] = useState([]);

  useEffect(() => {
    fetchOpportunities();
  }, []);

  const fetchOpportunities = async () => {
    const response = await axios.get("/api/opportunities");
    setOpportunities(response.data);
  };

  return (
    <div>
      <h1>Opportunity Directory</h1>
      <ul>
        {opportunities.map((opportunity) => (
          <li key={opportunity.id}>
            {opportunity.company} - {opportunity.position}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default OpportunityDirectory;
