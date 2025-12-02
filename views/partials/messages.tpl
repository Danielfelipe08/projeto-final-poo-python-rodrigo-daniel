% if defined('error') and error:
<div class="alert alert-error">
    {{error}}
</div>
% end

% if defined('success') and success:
<div class="alert alert-success">
    {{success}}
</div>
% end
