document.addEventListener("DOMContentLoaded", function () {
    const positionSelect = document.getElementById("position");
    const salaryInfo = document.getElementById("salary-info");

    positionSelect.addEventListener("change", function () {
        const position = positionSelect.value;
        let salaryText = "";

        switch (position) {
            case "Marketing Specialist":
                salaryText = "Salary: <b>$400,000</b> including compensations, rewards, and other entities.";
                break;
            case "Social Media Management":
                salaryText = "Salary: <b>$300,000</b> including compensations, rewards, and other entities.";
                break;
            case "Driver":
                salaryText = "Salary: <b>$150,000</b> including compensations and rewards.";
                break;
            default:
                salaryText = "";
        }

        salaryInfo.innerHTML = salaryText;
    });
});