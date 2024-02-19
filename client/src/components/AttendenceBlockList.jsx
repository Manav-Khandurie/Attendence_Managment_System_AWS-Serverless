import React from 'react';
import AttendanceBlock from './AttendanceBlock'; // Assuming the component is in the same directory

const AttendanceBlockList = ({ records, onUpdate, onDelete }) => {
  return (
    <div className="attendance-block-list">
      <h2>Attendance Records</h2>
      {records.map(record => (
        <AttendanceBlock
          key={record.uid}
          record={record}
          onUpdate={onUpdate}
          onDelete={onDelete}
        />
      ))}
    </div>
  );
};

export default AttendanceBlockList;
