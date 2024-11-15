document.addEventListener("DOMContentLoaded", function() {
    const studentList = document.getElementById("student-list");

    studentList.addEventListener("click", function(e) {
        if (e.target.classList.contains("edit-btn")) {
            const studentId = e.target.dataset.id;
            let marksInput = document.querySelector(`.marks-input[data-id="${studentId}"]`);
            let newMarks = marksInput.value;
            fetch(`/update_marks/${studentId}/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ marks: newMarks })
            });
        }

        if (e.target.classList.contains("delete-btn")) {
            const studentId = e.target.dataset.id;
            fetch(`/delete_student/${studentId}/`, { method: 'DELETE' });
            e.target.closest('tr').remove();
        }
    });

    document.getElementById("student-form").addEventListener("submit", function(e) {
        e.preventDefault();
        const name = document.getElementById("student-name").value;
        const subject = document.getElementById("student-subject").value;
        const marks = document.getElementById("student-marks").value;

        fetch("/add_student/", {
            method: "POST",
            body: JSON.stringify({ name, subject, marks }),
            headers: {
                "Content-Type": "application/json"
            }
        }).then(response => response.json())
          .then(data => {
              const row = document.createElement("tr");
              row.innerHTML = `<td>${name}</td><td>${subject}</td><td>${marks}</td><td>Actions</td>`;
              studentList.appendChild(row);
              document.getElementById("student-modal").style.display = "none";
          });
    });
});
