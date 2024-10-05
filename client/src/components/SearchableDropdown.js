import React, { useState } from 'react';

const symptoms = [
    'Fever',
    'Cough',
    'Fatigue',
    'Headache',
    'Sore Throat',
    'Shortness of Breath',
    'Loss of Taste or Smell',
    'Muscle Pain',
    'Nausea',
    'Diarrhea'
];

export default function SearchableDropdown() {
    const [searchTerm, setSearchTerm] = useState('');
    const [isDropdownOpen, setDropdownOpen] = useState(false);

    const handleInputChange = (event) => {
        setSearchTerm(event.target.value);
        setDropdownOpen(true); // Show dropdown when typing
    };

    const handleDropdownClose = () => {
        setDropdownOpen(false);
    };

    const filteredSymptoms = symptoms.filter(symptom =>
        symptom.toLowerCase().includes(searchTerm.toLowerCase())
    );

    return (
        <div className="flex items-center justify-center">
            <div className="relative">
                <input
                    type="text"
                    placeholder="Search for a symptom..."
                    value={searchTerm}
                    onChange={handleInputChange}
                    onFocus={() => setDropdownOpen(true)} // Show dropdown on focus
                    className="border p-2 rounded w-64"
                />
                {isDropdownOpen && (
                    <div className="absolute z-10 bg-white border border-gray-300 mt-1 rounded shadow-lg w-64">
                        {filteredSymptoms.length > 0 ? (
                            filteredSymptoms.map((symptom, index) => (
                                <div
                                    key={index}
                                    onClick={() => {
                                        setSearchTerm(symptom); // Set symptom on click
                                        handleDropdownClose(); // Close dropdown
                                    }}
                                    className="p-2 hover:bg-blue-100 cursor-pointer"
                                >
                                    {symptom}
                                </div>
                            ))
                        ) : (
                            <div className="p-2">No symptoms found</div>
                        )}
                    </div>
                )}
            </div>
        </div>
    );
}