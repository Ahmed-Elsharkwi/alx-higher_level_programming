$("#add_item").on("click", function() {
  const my_list = $(".my_list");
  my_list.append($("<li></li>").text("Item"));
});
