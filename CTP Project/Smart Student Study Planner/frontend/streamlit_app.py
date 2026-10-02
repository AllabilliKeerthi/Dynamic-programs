import sys
from pathlib import Path

import streamlit as st

# =========================================================
# PROJECT PATH
# =========================================================

PROJECT_ROOT = Path(__file__).resolve().parents[1]

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


# =========================================================
# IMPORT ALGORITHMS
# =========================================================

from app.algorithms import (
    backtracking_timetable,
    best_selection,
    greedy_schedule,
    knapsack,
    merge_sort,
)

# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Smart Student Study Planner",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded",
)


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown(
    """
<style>

.stApp {
    background:
        linear-gradient(
            135deg,
            #07111f 0%,
            #0b1728 45%,
            #111827 100%
        );
    color: #f8fafc;
}

.main {
    padding-top: 1rem;
}

.main-header {
    padding: 30px;
    border-radius: 20px;
    background:
        linear-gradient(
            135deg,
            #111827,
            #1e3a8a,
            #312e81
        );
    border: 1px solid #334155;
    margin-bottom: 25px;
    box-shadow:
        0 10px 30px rgba(0, 0, 0, 0.35);
}

.main-header h1 {
    color: #ffffff;
    font-size: 42px;
    margin-bottom: 8px;
    font-weight: 800;
}

.main-header p {
    color: #cbd5e1;
    font-size: 17px;
    margin-bottom: 0;
}

.section-title {
    color: #e2e8f0;
    font-size: 26px;
    font-weight: 700;
    margin-top: 20px;
    margin-bottom: 15px;
}

section[data-testid="stSidebar"] {
    background:
        linear-gradient(
            180deg,
            #0b1220,
            #111827
        );
    border-right: 1px solid #1e293b;
}

section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3 {
    color: #f8fafc;
}

label {
    color: #e2e8f0 !important;
}

div[data-baseweb="input"] {
    background-color: #111827;
}

.stButton > button {
    border-radius: 10px;
    border: 1px solid #475569;
    font-weight: 600;
    transition: all 0.2s ease;
}

.stButton > button:hover {
    border-color: #818cf8;
    transform: translateY(-1px);
}

div[data-testid="stMetric"] {
    background:
        linear-gradient(
            135deg,
            #111827,
            #172554
        );
    border: 1px solid #334155;
    padding: 15px;
    border-radius: 15px;
}

div[data-testid="stVerticalBlockBorderWrapper"] {
    border-radius: 15px;
}

div[data-testid="stAlert"] {
    border-radius: 12px;
}

.footer {
    margin-top: 45px;
    padding: 20px;
    text-align: center;
    border-top: 1px solid #334155;
    color: #94a3b8;
    font-size: 14px;
}

.footer strong {
    color: #c7d2fe;
}

</style>
""",
    unsafe_allow_html=True,
)


# =========================================================
# SESSION STATE
# =========================================================

if "tasks" not in st.session_state:
    st.session_state.tasks = []


# =========================================================
# HEADER
# =========================================================

st.markdown(
    """
<div class="main-header">
<h1>📚 Smart Student Study Planner</h1>
<p>Generate an optimized study plan using computational thinking and algorithmic techniques.</p>
</div>
""",
    unsafe_allow_html=True,
)


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown("## ⚙️ Planner Settings")

    st.markdown("---")

    st.markdown("### 👨‍🎓 Student Details")

    student_name = st.text_input(
        "Student Name",
        placeholder="Enter your name",
    )

    available_hours = st.number_input(
        "Available Study Hours",
        min_value=1,
        max_value=24,
        value=6,
        step=1,
    )

    st.markdown("---")

    st.markdown("### 🧠 Algorithms Used")

    st.write("🔹 Merge Sort")
    st.write("🔹 Greedy Algorithm")
    st.write("🔹 Dynamic Programming")
    st.write("🔹 Backtracking")
    st.write("🔹 Branch & Bound")

    st.markdown("---")

    st.markdown("### 📖 How It Works")

    st.write("1. Enter your study tasks.")
    st.write("2. Set difficulty and importance.")
    st.write("3. Enter required study hours.")
    st.write("4. Enter deadline information.")
    st.write("5. Generate the study plan.")


# =========================================================
# WELCOME MESSAGE
# =========================================================

if student_name.strip():
    st.markdown(
        f"### 👋 Welcome, {student_name.strip()}!"
    )
else:
    st.markdown("### 👋 Welcome, Student!")


# =========================================================
# ADD STUDY TASK
# =========================================================

st.markdown(
    '<div class="section-title">📝 Add Study Task</div>',
    unsafe_allow_html=True,
)


col1, col2 = st.columns(2)


with col1:

    task_name = st.text_input(
        "Task / Topic Name",
        placeholder="Example: Machine Learning",
    )

    subject = st.text_input(
        "Subject",
        placeholder="Example: Artificial Intelligence",
    )

    difficulty = st.slider(
        "Difficulty",
        min_value=1,
        max_value=10,
        value=5,
        help="1 = Very Easy, 10 = Very Difficult",
    )


with col2:

    importance = st.slider(
        "Importance",
        min_value=1,
        max_value=10,
        value=5,
        help="1 = Low Importance, 10 = Very Important",
    )

    hours = st.number_input(
        "Required Study Hours",
        min_value=1,
        max_value=24,
        value=2,
        step=1,
    )

    deadline = st.number_input(
        "Deadline in Days",
        min_value=1,
        max_value=365,
        value=7,
        step=1,
    )


# =========================================================
# ADD TASK BUTTON
# =========================================================

add_task = st.button(
    "➕ Add Task",
    use_container_width=True,
)


if add_task:

    if not task_name.strip():

        st.error(
            "⚠️ Please enter the Task / Topic Name."
        )

    elif not subject.strip():

        st.error(
            "⚠️ Please enter the Subject."
        )

    else:

        new_task = {
            "name": task_name.strip(),
            "subject": subject.strip(),
            "difficulty": int(difficulty),
            "importance": int(importance),
            "hours": int(hours),
            "deadline": int(deadline),
        }

        st.session_state.tasks.append(
            new_task
        )

        st.success(
            f"✅ '{task_name.strip()}' has been added successfully!"
        )


# =========================================================
# DISPLAY TASKS
# =========================================================

if st.session_state.tasks:

    st.markdown(
        '<div class="section-title">📋 Your Study Tasks</div>',
        unsafe_allow_html=True,
    )

    for index, task in enumerate(
        st.session_state.tasks,
        start=1,
    ):

        with st.container(border=True):

            col1, col2, col3, col4, col5, col6 = (
                st.columns(6)
            )

            with col1:
                st.markdown(
                    f"**{index}. {task['name']}**"
                )

            with col2:
                st.write(
                    f"📚 {task['subject']}"
                )

            with col3:
                st.write(
                    f"🎯 Difficulty: "
                    f"{task['difficulty']}/10"
                )

            with col4:
                st.write(
                    f"⭐ Importance: "
                    f"{task['importance']}/10"
                )

            with col5:
                st.write(
                    f"⏱️ {task['hours']} hour(s)"
                )

            with col6:
                st.write(
                    f"📅 {task['deadline']} day(s)"
                )


# =========================================================
# TASK MANAGEMENT
# =========================================================

if st.session_state.tasks:

    st.markdown("")

    col1, col2 = st.columns(2)

    with col1:

        clear_tasks = st.button(
            "🗑️ Clear All Tasks",
            use_container_width=True,
        )

    with col2:

        generate_plan = st.button(
            "🚀 Generate Study Plan",
            use_container_width=True,
        )

    if clear_tasks:

        st.session_state.tasks = []

        st.success(
            "🗑️ All tasks have been cleared."
        )

        st.rerun()

else:

    generate_plan = False

    st.info(
        "💡 Add at least one study task to generate your study plan."
    )


# =========================================================
# GENERATE STUDY PLAN
# =========================================================

if generate_plan:

    tasks = st.session_state.tasks

    available = int(
        available_hours
    )

    # =====================================================
    # MERGE SORT
    # =====================================================

    sorted_tasks = sorted(
        tasks,
        key=lambda task: task["deadline"],
    )

    deadline_values = [
        task["deadline"]
        for task in tasks
    ]

    sorted_deadlines = merge_sort(
        deadline_values
    )

    # =====================================================
    # GREEDY
    # =====================================================

    greedy_input = [
        (
            task["name"],
            task["hours"],
        )
        for task in tasks
    ]

    greedy_result = greedy_schedule(
        greedy_input,
        available,
    )

    # =====================================================
    # KNAPSACK
    # =====================================================

    values = [
        task["importance"]
        for task in tasks
    ]

    weights = [
        task["hours"]
        for task in tasks
    ]

    knapsack_value = knapsack(
        values,
        weights,
        available,
    )

    # =====================================================
    # BACKTRACKING
    # =====================================================

    backtracking_tasks = [
        (
            task["name"],
            task["hours"],
        )
        for task in sorted_tasks
    ]

    timetable = backtracking_timetable(
        backtracking_tasks,
        available,
    )

    # =====================================================
    # BRANCH & BOUND
    # =====================================================

    branch_bound_value = best_selection(
        values,
        weights,
        available,
    )

    # =====================================================
    # RESULTS
    # =====================================================

    st.markdown(
        '<div class="section-title">📊 Study Plan Results</div>',
        unsafe_allow_html=True,
    )

    # =====================================================
    # SUMMARY METRICS
    # =====================================================

    total_task_hours = sum(
        task["hours"]
        for task in tasks
    )

    total_importance = sum(
        task["importance"]
        for task in tasks
    )

    remaining_hours = max(
        0,
        available - total_task_hours,
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "📚 Total Tasks",
            len(tasks),
        )

    with col2:

        st.metric(
            "⏱️ Available Hours",
            available,
        )

    with col3:

        st.metric(
            "⭐ Total Importance",
            total_importance,
        )

    with col4:

        st.metric(
            "🕐 Remaining Hours",
            remaining_hours,
        )

    # =====================================================
    # 1. MERGE SORT
    # =====================================================

    with st.container(border=True):

        st.markdown(
            "### 1️⃣ Merge Sort"
        )

        st.write(
            "Tasks are sorted according to their deadline."
        )

        st.write(
            f"Sorted deadline values: {sorted_deadlines}"
        )

        st.write(
            "**Optimized Study Order:**"
        )

        for index, task in enumerate(
            sorted_tasks,
            start=1,
        ):

            st.write(
                f"{index}. **{task['name']}** — "
                f"{task['deadline']} day(s) deadline"
            )

    # =====================================================
    # 2. GREEDY
    # =====================================================

    with st.container(border=True):

        st.markdown(
            "### 2️⃣ Greedy Algorithm"
        )

        st.write(
            "The Greedy algorithm selects tasks while "
            "respecting the available study hours."
        )

        if greedy_result:

            st.write(
                "**Selected Tasks:**"
            )

            for task_name in greedy_result:

                st.write(
                    f"✅ {task_name}"
                )

        else:

            st.warning(
                "No task could be selected within the available hours."
            )

    # =====================================================
    # 3. KNAPSACK
    # =====================================================

    with st.container(border=True):

        st.markdown(
            "### 3️⃣ Dynamic Programming — Knapsack"
        )

        st.write(
            "Knapsack maximizes the total importance "
            "of selected tasks within the available "
            "study-hour capacity."
        )

        st.metric(
            "Maximum Study Value",
            knapsack_value,
        )

        st.write(
            f"Available capacity: {available} hour(s)"
        )

    # =====================================================
    # 4. BACKTRACKING
    # =====================================================

    with st.container(border=True):

        st.markdown(
            "### 4️⃣ Backtracking"
        )

        st.write(
            "Backtracking tries different combinations "
            "of study tasks while respecting their actual "
            "study hours and available time."
        )

        if timetable:

            st.write(
                "**Generated Timetable:**"
            )

            for index, topic in enumerate(
                timetable,
                start=1,
            ):

                st.write(
                    f"🕐 Slot {index}: {topic}"
                )

        else:

            st.warning(
                "Unable to create a timetable with the available hours."
            )

    # =====================================================
    # 5. BRANCH & BOUND
    # =====================================================

    with st.container(border=True):

        st.markdown(
            "### 5️⃣ Branch & Bound"
        )

        st.write(
            "Branch & Bound explores different task "
            "combinations and prunes branches that "
            "cannot improve the current result."
        )

        st.metric(
            "Best Selection Value",
            branch_bound_value,
        )

    # =====================================================
    # OPTIMIZED STUDY PLAN
    # =====================================================

    st.markdown(
        '<div class="section-title">🎯 Optimized Study Plan</div>',
        unsafe_allow_html=True,
    )

    optimized_tasks = sorted(
        tasks,
        key=lambda task: (
            -task["importance"],
            task["deadline"],
        ),
    )

    remaining = available

    selected_tasks = []

    for task in optimized_tasks:

        if task["hours"] <= remaining:

            selected_tasks.append(
                task
            )

            remaining -= task["hours"]

    if selected_tasks:

        for index, task in enumerate(
            selected_tasks,
            start=1,
        ):

            with st.container(border=True):

                col1, col2, col3, col4 = (
                    st.columns(4)
                )

                with col1:

                    st.markdown(
                        f"**{index}. {task['name']}**"
                    )

                with col2:

                    st.write(
                        f"📚 {task['subject']}"
                    )

                with col3:

                    st.write(
                        f"⏱️ {task['hours']} hour(s)"
                    )

                with col4:

                    st.write(
                        f"⭐ Importance: "
                        f"{task['importance']}/10"
                    )

    else:

        st.warning(
            "No task fits within the available study hours."
        )

    # =====================================================
    # DIFFICULT TOPICS
    # =====================================================

    st.markdown(
        '<div class="section-title">🔥 Difficult Topics</div>',
        unsafe_allow_html=True,
    )

    difficult_tasks = [
        task
        for task in tasks
        if task["difficulty"] >= 7
    ]

    if difficult_tasks:

        for task in difficult_tasks:

            with st.container(border=True):

                st.write(
                    f"🔥 **{task['name']}**"
                )

                st.write(
                    f"Subject: {task['subject']}"
                )

                st.write(
                    f"Difficulty: "
                    f"{task['difficulty']}/10"
                )

                st.write(
                    f"Importance: "
                    f"{task['importance']}/10"
                )

    else:

        st.info(
            "No highly difficult topics were identified."
        )

    # =====================================================
    # TASK SUMMARY
    # =====================================================

    st.markdown(
        '<div class="section-title">📈 Task Summary</div>',
        unsafe_allow_html=True,
    )

    for task in tasks:

        with st.container(border=True):

            st.markdown(
                f"### {task['name']}"
            )

            col1, col2, col3 = st.columns(3)

            with col1:

                st.write(
                    f"📚 Subject: {task['subject']}"
                )

                st.write(
                    f"🎯 Difficulty: "
                    f"{task['difficulty']}/10"
                )

            with col2:

                st.write(
                    f"⭐ Importance: "
                    f"{task['importance']}/10"
                )

                st.write(
                    f"⏱️ Study Hours: "
                    f"{task['hours']}"
                )

            with col3:

                st.write(
                    f"📅 Deadline: "
                    f"{task['deadline']} day(s)"
                )

                if task["difficulty"] >= 8:

                    st.write(
                        "🔥 High difficulty"
                    )

                elif task["difficulty"] >= 5:

                    st.write(
                        "⚠️ Medium difficulty"
                    )

                else:

                    st.write(
                        "✅ Low difficulty"
                    )


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    """
<div class="footer">
<strong>📚 Smart Student Study Planner</strong>
<br><br>
Computational Thinking & Programming Project
<br>
Merge Sort • Greedy • Dynamic Programming • Backtracking • Branch & Bound
<br><br>
Built with Python and Streamlit
</div>
""",
    unsafe_allow_html=True,
)