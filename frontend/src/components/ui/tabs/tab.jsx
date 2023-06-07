import React, { useState } from "react";
import classes from "./tab.module.css";
import { Tab, Box } from "@mui/material";
import { TabContext, TabList, TabPanel } from "@mui/lab";

const tabs = {
  items: ["All Records", "Arrchive"],
  content: [["All"], ["Archive"]],
};

const DefaultTabs = () => {
  const [tabIndex, setTabIndex] = useState(0);

  return (
    <TabContext value={tabIndex}>
      <Box sx={{ borderBottom: 1, borderColor: "divider" }}>
        <TabList onChange={(event, newValue) => setTabIndex(newValue)}>
          {tabs.items.map((items, index) => (
            <Tab label={items} value={index} />
          ))}
        </TabList>
      </Box>
      {tabs.content.map((content, index) => (
        <TabPanel value={index}>{content}</TabPanel>
      ))}
    </TabContext>
  );
};

export default DefaultTabs;
