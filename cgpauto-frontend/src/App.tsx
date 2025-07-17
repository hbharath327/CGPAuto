import React, { useState } from 'react';
import './App.css';

function App() {
  const [files, setFiles] = useState<FileList | null>(null);
  const [result, setResult] = useState<any>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setFiles(e.target.files);
    setResult(null);
    setError(null);
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!files || files.length === 0) {
      setError('Please select at least one PDF file.');
      return;
    }
    setLoading(true);
    setError(null);
    setResult(null);
    const formData = new FormData();
    Array.from(files).forEach((file) => {
      formData.append('files', file);
    });
    try {
      const response = await fetch('http://127.0.0.1:8000/upload', {
        method: 'POST',
        body: formData,
      });
      if (!response.ok) {
        throw new Error('Failed to upload and calculate CGPA.');
      }
      const data = await response.json();
      setResult(data);
    } catch (err: any) {
      setError(err.message || 'Unknown error');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="App">
      <h1>CGPA Calculator</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="file"
          accept="application/pdf"
          multiple
          onChange={handleFileChange}
        />
        <button type="submit" disabled={loading}>
          {loading ? 'Calculating...' : 'Upload & Calculate'}
        </button>
      </form>
      {error && <div style={{ color: 'red', marginTop: 10 }}>{error}</div>}
      {result && (
        <div style={{ marginTop: 20 }}>
          <h2>Result</h2>
          <div><strong>CGPA:</strong> {result.cgpa?.toFixed(2)}</div>
          <div>
            <strong>SGPA by Semester:</strong>
            <ul>
              {result.sgpas?.map((sgpa: number | null, idx: number) =>
                sgpa !== null ? (
                  <li key={idx}>Semester {idx + 1}: {sgpa.toFixed(2)}</li>
                ) : null
              )}
            </ul>
          </div>
          <div style={{ marginTop: 30 }}>
            <h2>Detailed Semester-wise Results</h2>
            {Object.entries(result.semesters || {}).map(([sem, subjects]: [string, any[]]) => (
              <div key={sem} style={{ marginBottom: 24, border: '1px solid #ccc', borderRadius: 8, padding: 12 }}>
                <h3>Semester {sem}</h3>
                {subjects.length === 0 ? (
                  <div>No data for this semester.</div>
                ) : (
                  <table style={{ width: '100%', borderCollapse: 'collapse' }}>
                    <thead>
                      <tr>
                        <th style={{ border: '1px solid #ccc', padding: 4 }}>Subject Code</th>
                        <th style={{ border: '1px solid #ccc', padding: 4 }}>Subject Name</th>
                        <th style={{ border: '1px solid #ccc', padding: 4 }}>Marks</th>
                        <th style={{ border: '1px solid #ccc', padding: 4 }}>Credits</th>
                        <th style={{ border: '1px solid #ccc', padding: 4 }}>Grade Point</th>
                      </tr>
                    </thead>
                    <tbody>
                      {subjects.map((sub, i) => (
                        <tr key={i}>
                          <td style={{ border: '1px solid #ccc', padding: 4 }}>{sub.subject_code}</td>
                          <td style={{ border: '1px solid #ccc', padding: 4 }}>{sub.subject_name}</td>
                          <td style={{ border: '1px solid #ccc', padding: 4 }}>{sub.marks}</td>
                          <td style={{ border: '1px solid #ccc', padding: 4 }}>{sub.credits}</td>
                          <td style={{ border: '1px solid #ccc', padding: 4 }}>{sub.grade_point}</td>
                        </tr>
                      ))}
                    </tbody>
                  </table>
                )}
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}

export default App;
