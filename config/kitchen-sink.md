---
layout: home
---

<div class="container">
  <div class="row">
<% @glyphs.each do |name, value|
  unless name.end_with? "-square"
%>      <i class="ai ai-<%= name %> ai-4x"></i>
<% end
end%>
      <br />
<% @glyphs.each do |name, value|
  if name.end_with? "-square"
%>      <i class="ai ai-<%= name %> ai-4x"></i>
<% end
end%>
  </div>
</div>


