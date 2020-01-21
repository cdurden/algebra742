var options = {
      group: 'sortable',
      animation: 100
};
options['onAdd'] = function(evt) {
    var returnItem = $("li",evt.to).eq(evt.newIndex+1);
    var swapTarget = $(evt.from).children().eq(evt.oldIndex);
    console.log({
      'event': name,
      'this': this,
      'item': evt.item,
      'from': evt.from,
      'to': evt.to,
      'oldIndex': evt.oldIndex,
      'newIndex': evt.newIndex,
      'returnItem': returnItem,
      'swapTarget': swapTarget,
    });
    $(returnItem).remove();
    if (swapTarget.length != 0) {
        $(swapTarget).before(returnItem);
        console.log(swapTarget);
    } else {
        $(evt.from).append(returnItem);
        console.log(swapTarget);
    }
}
$(function() {
    $("#sortable-blanks").sortable(options);
    $("#sortable-items").sortable(options);
});
