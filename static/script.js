document.addEventListener("DOMContentLoaded", function () {
    const positionSelect = document.getElementById("position");
    const salaryInfo = document.getElementById("salary-info");
    const jobApplicationForm = document.getElementById("jobApplicationForm");
    const fileInput = document.getElementById("file");

    // Job positions and corresponding salaries
    const salaries = {
        "Marketing Specialist": "Salary: <b>$400,000</b> including compensations, rewards, and other entities.",
        "Social Media Management": "Salary: <b>$300,000</b> including compensations, rewards, and other entities.",
        "Driver": "Salary: <b>$150,000</b> including compensations and rewards."
    };

    // Show salary info when job position is selected
    positionSelect.addEventListener("change", function () {
        const selectedPosition = positionSelect.value;

        if (salaries[selectedPosition]) {
            salaryInfo.innerHTML = salaries[selectedPosition];
            salaryInfo.style.display = "block"; // Show salary info
        } else {
            salaryInfo.innerHTML = ""; // Clear salary info if no selection
            salaryInfo.style.display = "none";
        }
    });

    // File validation: Allow only PDF, DOC, and DOCX
    jobApplicationForm.addEventListener("submit", function (event) {
        const filePath = fileInput.value;
        const allowedExtensions = /(\.pdf|\.doc|\.docx)$/i;

        if (!allowedExtensions.exec(filePath)) {
            alert("Invalid file type. Please upload a PDF or DOCX file.");
            fileInput.value = ""; // Clear file input
            event.preventDefault(); // Stop form submission
        }
    });
});