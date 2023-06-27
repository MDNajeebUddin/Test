$(document).ready(function() {
    $('#loadDataBtn').click(function() {
        $.ajax({
            url: '/api/data',
            type: 'GET',
            success: function(data) {
                // Populate the DataTable
                $('#dataTableContainer').html('<table id="dataTable"></table>');
                $('#dataTable').DataTable({
                    data: data,
                    columns: [
                        { title: 'ID', data: 'id' },
                        { title: 'Name', data: 'name' },
                        { title: 'Age', data: 'age' }
                    ]
                });

                // Generate the graph
                var names = data.map(function(item) {
                    return item.name;
                });
                var ages = data.map(function(item) {
                    return item.age;
                });
                var graphData = [
                    {
                        x: names,
                        y: ages,
                        type: 'bar'
                    }
                ];
                Plotly.newPlot('graphContainer', graphData);
            }
        });
    });
});
