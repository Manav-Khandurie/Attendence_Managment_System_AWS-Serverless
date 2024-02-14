import axios from 'axios';

const API_ENDPOINT = process.env.REACT_APP_API_ENDPOINT;

export const fetchAttendanceRecords = async () => {
  try {
    const response = await axios.post(`${API_ENDPOINT}`, { operation : "fetch" });
    return response.data.body;
  } catch (error) {
    console.error('Error fetching attendance records:', error);
    throw error;
  }
};
