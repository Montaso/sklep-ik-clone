<?php

// This file has been auto-generated by the Symfony Dependency Injection Component for internal use.

if (\class_exists(\ContainerXd9nm7z\appDevDebugProjectContainer::class, false)) {
    // no-op
} elseif (!include __DIR__.'/ContainerXd9nm7z/appDevDebugProjectContainer.php') {
    touch(__DIR__.'/ContainerXd9nm7z.legacy');

    return;
}

if (!\class_exists(appDevDebugProjectContainer::class, false)) {
    \class_alias(\ContainerXd9nm7z\appDevDebugProjectContainer::class, appDevDebugProjectContainer::class, false);
}

return new \ContainerXd9nm7z\appDevDebugProjectContainer([
    'container.build_hash' => 'Xd9nm7z',
    'container.build_id' => '0d0ebce1',
    'container.build_time' => 1733069423,
], __DIR__.\DIRECTORY_SEPARATOR.'ContainerXd9nm7z');
