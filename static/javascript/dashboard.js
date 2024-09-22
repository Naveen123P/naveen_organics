document.addEventListener('DOMContentLoaded', function () {
    // Fetch user details and recent activity
    fetchUserDetails();
    fetchRecentActivity();
});

function fetchUserDetails() {
    // Simulated user details; replace with actual data from your backend
    var userData = {
        username: 'JohnDoe',
        email: 'john.doe@example.com'
    };

    // Populate user details on the dashboard
    document.getElementById('username').textContent = userData.username;
    document.getElementById('user-username').textContent = userData.username;
    document.getElementById('user-email').textContent = userData.email;
}

function fetchRecentActivity() {
    // Simulated recent activity; replace with actual data from your backend
    var recentActivityData = ['Logged in', 'Viewed profile', 'Made a purchase'];

    // Populate recent activity on the dashboard
    var recentActivityList = document.getElementById('recent-activity');
    recentActivityData.forEach(function (activity) {
        var listItem = document.createElement('li');
        listItem.textContent = activity;
        recentActivityList.appendChild(listItem);
    });
}

function logout() {
    // Perform logout actions (e.g., redirect to logout endpoint)
    // Simulated logout; replace with actual logout logic
    alert('Logged out successfully');
    // You might want to redirect the user to the logout endpoint or login page
    // window.location.href = '/logout/';
}
